if(typeof module!=="undefined"&&module.exports){this["encoding-indexes"]=require("./encoding-indexes.js")["encoding-indexes"];}
(function(global){'use strict';function inRange(a,min,max){return min<=a&&a<=max;}
function div(n,d){return Math.floor(n/d);}
var EOF_byte=-1;var EOF_code_point=-1;function ByteInputStream(bytes){var pos=0;this.get=function(){return(pos>=bytes.length)?EOF_byte:Number(bytes[pos]);};this.offset=function(n){pos+=n;if(pos<0){throw new Error('Seeking past start of the buffer');}
if(pos>bytes.length){throw new Error('Seeking past EOF');}};this.match=function(test){if(test.length>pos+bytes.length){return false;}
var i;for(i=0;i<test.length;i+=1){if(Number(bytes[pos+i])!==test[i]){return false;}}
return true;};}
function ByteOutputStream(bytes){var pos=0;this.emit=function(var_args){var last=EOF_byte;var i;for(i=0;i<arguments.length;++i){last=Number(arguments[i]);bytes[pos++]=last;}
return last;};}
function CodePointInputStream(string){function stringToCodePoints(string){var cps=[];var i=0,n=string.length;while(i<string.length){var c=string.charCodeAt(i);if(!inRange(c,0xD800,0xDFFF)){cps.push(c);}else if(inRange(c,0xDC00,0xDFFF)){cps.push(0xFFFD);}else{if(i===n-1){cps.push(0xFFFD);}else{var d=string.charCodeAt(i+1);if(inRange(d,0xDC00,0xDFFF)){var a=c&0x3FF;var b=d&0x3FF;i+=1;cps.push(0x10000+(a<<10)+b);}else{cps.push(0xFFFD);}}}
i+=1;}
return cps;}
var pos=0;var cps=stringToCodePoints(string);this.offset=function(n){pos+=n;if(pos<0){throw new Error('Seeking past start of the buffer');}
if(pos>cps.length){throw new Error('Seeking past EOF');}};this.get=function(){if(pos>=cps.length){return EOF_code_point;}
return cps[pos];};}
function CodePointOutputStream(){var string='';this.string=function(){return string;};this.emit=function(c){if(c<=0xFFFF){string+=String.fromCharCode(c);}else{c-=0x10000;string+=String.fromCharCode(0xD800+((c>>10)&0x3ff));string+=String.fromCharCode(0xDC00+(c&0x3ff));}};}
function EncodingError(message){this.name='EncodingError';this.message=message;this.code=0;}
EncodingError.prototype=Error.prototype;function decoderError(fatal,opt_code_point){if(fatal){throw new EncodingError('Decoder error');}
return opt_code_point||0xFFFD;}
function encoderError(code_point){throw new EncodingError('The code point '+code_point+
' could not be encoded.');}
function getEncoding(label){label=String(label).trim().toLowerCase();if(Object.prototype.hasOwnProperty.call(label_to_encoding,label)){return label_to_encoding[label];}
return null;}
var encodings=[{"encodings":[{"labels":["unicode-1-1-utf-8","utf-8","utf8"],"name":"utf-8"}],"heading":"The Encoding"},{"encodings":[{"labels":["866","cp866","csibm866","ibm866"],"name":"ibm866"},{"labels":["csisolatin2","iso-8859-2","iso-ir-101","iso8859-2","iso88592","iso_8859-2","iso_8859-2:1987","l2","latin2"],"name":"iso-8859-2"},{"labels":["csisolatin3","iso-8859-3","iso-ir-109","iso8859-3","iso88593","iso_8859-3","iso_8859-3:1988","l3","latin3"],"name":"iso-8859-3"},{"labels":["csisolatin4","iso-8859-4","iso-ir-110","iso8859-4","iso88594","iso_8859-4","iso_8859-4:1988","l4","latin4"],"name":"iso-8859-4"},{"labels":["csisolatincyrillic","cyrillic","iso-8859-5","iso-ir-144","iso8859-5","iso88595","iso_8859-5","iso_8859-5:1988"],"name":"iso-8859-5"},{"labels":["arabic","asmo-708","csiso88596e","csiso88596i","csisolatinarabic","ecma-114","iso-8859-6","iso-8859-6-e","iso-8859-6-i","iso-ir-127","iso8859-6","iso88596","iso_8859-6","iso_8859-6:1987"],"name":"iso-8859-6"},{"labels":["csisolatingreek","ecma-118","elot_928","greek","greek8","iso-8859-7","iso-ir-126","iso8859-7","iso88597","iso_8859-7","iso_8859-7:1987","sun_eu_greek"],"name":"iso-8859-7"},{"labels":["csiso88598e","csisolatinhebrew","hebrew","iso-8859-8","iso-8859-8-e","iso-ir-138","iso8859-8","iso88598","iso_8859-8","iso_8859-8:1988","visual"],"name":"iso-8859-8"},{"labels":["csiso88598i","iso-8859-8-i","logical"],"name":"iso-8859-8-i"},{"labels":["csisolatin6","iso-8859-10","iso-ir-157","iso8859-10","iso885910","l6","latin6"],"name":"iso-8859-10"},{"labels":["iso-8859-13","iso8859-13","iso885913"],"name":"iso-8859-13"},{"labels":["iso-8859-14","iso8859-14","iso885914"],"name":"iso-8859-14"},{"labels":["csisolatin9","iso-8859-15","iso8859-15","iso885915","iso_8859-15","l9"],"name":"iso-8859-15"},{"labels":["iso-8859-16"],"name":"iso-8859-16"},{"labels":["cskoi8r","koi","koi8","koi8-r","koi8_r"],"name":"koi8-r"},{"labels":["koi8-u"],"name":"koi8-u"},{"labels":["csmacintosh","mac","macintosh","x-mac-roman"],"name":"macintosh"},{"labels":["dos-874","iso-8859-11","iso8859-11","iso885911","tis-620","windows-874"],"name":"windows-874"},{"labels":["cp1250","windows-1250","x-cp1250"],"name":"windows-1250"},{"labels":["cp1251","windows-1251","x-cp1251"],"name":"windows-1251"},{"labels":["ansi_x3.4-1968","ascii","cp1252","cp819","csisolatin1","ibm819","iso-8859-1","iso-ir-100","iso8859-1","iso88591","iso_8859-1","iso_8859-1:1987","l1","latin1","us-ascii","windows-1252","x-cp1252"],"name":"windows-1252"},{"labels":["cp1253","windows-1253","x-cp1253"],"name":"windows-1253"},{"labels":["cp1254","csisolatin5","iso-8859-9","iso-ir-148","iso8859-9","iso88599","iso_8859-9","iso_8859-9:1989","l5","latin5","windows-1254","x-cp1254"],"name":"windows-1254"},{"labels":["cp1255","windows-1255","x-cp1255"],"name":"windows-1255"},{"labels":["cp1256","windows-1256","x-cp1256"],"name":"windows-1256"},{"labels":["cp1257","windows-1257","x-cp1257"],"name":"windows-1257"},{"labels":["cp1258","windows-1258","x-cp1258"],"name":"windows-1258"},{"labels":["x-mac-cyrillic","x-mac-ukrainian"],"name":"x-mac-cyrillic"}],"heading":"Legacy single-byte encodings"},{"encodings":[{"labels":["chinese","csgb2312","csiso58gb231280","gb18030","gb2312","gb_2312","gb_2312-80","gbk","iso-ir-58","x-gbk"],"name":"gb18030"},{"labels":["hz-gb-2312"],"name":"hz-gb-2312"}],"heading":"Legacy multi-byte Chinese (simplified) encodings"},{"encodings":[{"labels":["big5","big5-hkscs","cn-big5","csbig5","x-x-big5"],"name":"big5"}],"heading":"Legacy multi-byte Chinese (traditional) encodings"},{"encodings":[{"labels":["cseucpkdfmtjapanese","euc-jp","x-euc-jp"],"name":"euc-jp"},{"labels":["csiso2022jp","iso-2022-jp"],"name":"iso-2022-jp"},{"labels":["csshiftjis","ms_kanji","shift-jis","shift_jis","sjis","windows-31j","x-sjis"],"name":"shift_jis"}],"heading":"Legacy multi-byte Japanese encodings"},{"encodings":[{"labels":["cseuckr","csksc56011987","euc-kr","iso-ir-149","korean","ks_c_5601-1987","ks_c_5601-1989","ksc5601","ksc_5601","windows-949"],"name":"euc-kr"}],"heading":"Legacy multi-byte Korean encodings"},{"encodings":[{"labels":["csiso2022kr","iso-2022-cn","iso-2022-cn-ext","iso-2022-kr"],"name":"replacement"},{"labels":["utf-16be"],"name":"utf-16be"},{"labels":["utf-16","utf-16le"],"name":"utf-16le"},{"labels":["x-user-defined"],"name":"x-user-defined"}],"heading":"Legacy miscellaneous encodings"}];var name_to_encoding={};var label_to_encoding={};encodings.forEach(function(category){category['encodings'].forEach(function(encoding){name_to_encoding[encoding['name']]=encoding;encoding['labels'].forEach(function(label){label_to_encoding[label]=encoding;});});});function indexCodePointFor(pointer,index){if(!index)return null;return index[pointer]||null;}
function indexPointerFor(code_point,index){var pointer=index.indexOf(code_point);return pointer===-1?null:pointer;}
function index(name){if(!('encoding-indexes'in global))
throw new Error("Indexes missing. Did you forget to include encoding-indexes.js?");return global['encoding-indexes'][name];}
function indexGB18030CodePointFor(pointer){if((pointer>39419&&pointer<189000)||(pointer>1237575)){return null;}
var offset=0,code_point_offset=0,idx=index('gb18030');var i;for(i=0;i<idx.length;++i){var entry=idx[i];if(entry[0]<=pointer){offset=entry[0];code_point_offset=entry[1];}else{break;}}
return code_point_offset+pointer-offset;}
function indexGB18030PointerFor(code_point){var offset=0,pointer_offset=0,idx=index('gb18030');var i;for(i=0;i<idx.length;++i){var entry=idx[i];if(entry[1]<=code_point){offset=entry[1];pointer_offset=entry[0];}else{break;}}
return pointer_offset+code_point-offset;}
var DEFAULT_ENCODING='utf-8';function TextDecoder(opt_encoding,options){if(!(this instanceof TextDecoder)){return new TextDecoder(opt_encoding,options);}
opt_encoding=opt_encoding?String(opt_encoding):DEFAULT_ENCODING;options=Object(options);this._encoding=getEncoding(opt_encoding);if(this._encoding===null||this._encoding.name==='replacement')
throw new TypeError('Unknown encoding: '+opt_encoding);if(!this._encoding.getDecoder)
throw new Error('Decoder not present. Did you forget to include encoding-indexes.js?');this._streaming=false;this._BOMseen=false;this._decoder=null;this._options={fatal:Boolean(options.fatal)};if(Object.defineProperty){Object.defineProperty(this,'encoding',{get:function(){return this._encoding.name;}});}else{this.encoding=this._encoding.name;}
return this;}
TextDecoder.prototype={decode:function decode(opt_view,options){if(opt_view&&!('buffer'in opt_view&&'byteOffset'in opt_view&&'byteLength'in opt_view)){throw new TypeError('Expected ArrayBufferView');}else if(!opt_view){opt_view=new Uint8Array(0);}
options=Object(options);if(!this._streaming){this._decoder=this._encoding.getDecoder(this._options);this._BOMseen=false;}
this._streaming=Boolean(options.stream);var bytes=new Uint8Array(opt_view.buffer,opt_view.byteOffset,opt_view.byteLength);var input_stream=new ByteInputStream(bytes);var output_stream=new CodePointOutputStream();var code_point;while(input_stream.get()!==EOF_byte){code_point=this._decoder.decode(input_stream);if(code_point!==null&&code_point!==EOF_code_point){output_stream.emit(code_point);}}
if(!this._streaming){do{code_point=this._decoder.decode(input_stream);if(code_point!==null&&code_point!==EOF_code_point){output_stream.emit(code_point);}}while(code_point!==EOF_code_point&&input_stream.get()!=EOF_byte);this._decoder=null;}
var result=output_stream.string();if(!this._BOMseen&&result.length){this._BOMseen=true;if(['utf-8','utf-16le','utf-16be'].indexOf(this.encoding)!==-1&&result.charCodeAt(0)===0xFEFF){result=result.substring(1);}}
return result;}};function TextEncoder(opt_encoding,options){if(!(this instanceof TextEncoder)){return new TextEncoder(opt_encoding,options);}
opt_encoding=opt_encoding?String(opt_encoding):DEFAULT_ENCODING;options=Object(options);this._encoding=getEncoding(opt_encoding);var allowLegacyEncoding=options.NONSTANDARD_allowLegacyEncoding;var isLegacyEncoding=(this._encoding.name!=='utf-8'&&this._encoding.name!=='utf-16le'&&this._encoding.name!=='utf-16be');if(this._encoding===null||(isLegacyEncoding&&!allowLegacyEncoding))
throw new TypeError('Unknown encoding: '+opt_encoding);if(!this._encoding.getEncoder)
throw new Error('Encoder not present. Did you forget to include encoding-indexes.js?');this._streaming=false;this._encoder=null;this._options={fatal:Boolean(options.fatal)};if(Object.defineProperty){Object.defineProperty(this,'encoding',{get:function(){return this._encoding.name;}});}else{this.encoding=this._encoding.name;}
return this;}
TextEncoder.prototype={encode:function encode(opt_string,options){opt_string=opt_string?String(opt_string):'';options=Object(options);if(!this._streaming){this._encoder=this._encoding.getEncoder(this._options);}
this._streaming=Boolean(options.stream);var bytes=[];var output_stream=new ByteOutputStream(bytes);var input_stream=new CodePointInputStream(opt_string);while(input_stream.get()!==EOF_code_point){this._encoder.encode(output_stream,input_stream);}
if(!this._streaming){var last_byte;do{last_byte=this._encoder.encode(output_stream,input_stream);}while(last_byte!==EOF_byte);this._encoder=null;}
return new Uint8Array(bytes);}};function UTF8Decoder(options){var fatal=options.fatal;var utf8_code_point=0,utf8_bytes_needed=0,utf8_bytes_seen=0,utf8_lower_boundary=0;this.decode=function(byte_pointer){var bite=byte_pointer.get();if(bite===EOF_byte){if(utf8_bytes_needed!==0){return decoderError(fatal);}
return EOF_code_point;}
byte_pointer.offset(1);if(utf8_bytes_needed===0){if(inRange(bite,0x00,0x7F)){return bite;}
if(inRange(bite,0xC2,0xDF)){utf8_bytes_needed=1;utf8_lower_boundary=0x80;utf8_code_point=bite-0xC0;}else if(inRange(bite,0xE0,0xEF)){utf8_bytes_needed=2;utf8_lower_boundary=0x800;utf8_code_point=bite-0xE0;}else if(inRange(bite,0xF0,0xF4)){utf8_bytes_needed=3;utf8_lower_boundary=0x10000;utf8_code_point=bite-0xF0;}else{return decoderError(fatal);}
utf8_code_point=utf8_code_point*Math.pow(64,utf8_bytes_needed);return null;}
if(!inRange(bite,0x80,0xBF)){utf8_code_point=0;utf8_bytes_needed=0;utf8_bytes_seen=0;utf8_lower_boundary=0;byte_pointer.offset(-1);return decoderError(fatal);}
utf8_bytes_seen+=1;utf8_code_point=utf8_code_point+(bite-0x80)*Math.pow(64,utf8_bytes_needed-utf8_bytes_seen);if(utf8_bytes_seen!==utf8_bytes_needed){return null;}
var code_point=utf8_code_point;var lower_boundary=utf8_lower_boundary;utf8_code_point=0;utf8_bytes_needed=0;utf8_bytes_seen=0;utf8_lower_boundary=0;if(inRange(code_point,lower_boundary,0x10FFFF)&&!inRange(code_point,0xD800,0xDFFF)){return code_point;}
return decoderError(fatal);};}
function UTF8Encoder(options){var fatal=options.fatal;this.encode=function(output_byte_stream,code_point_pointer){var code_point=code_point_pointer.get();if(code_point===EOF_code_point){return EOF_byte;}
code_point_pointer.offset(1);if(inRange(code_point,0xD800,0xDFFF)){return encoderError(code_point);}
if(inRange(code_point,0x0000,0x007f)){return output_byte_stream.emit(code_point);}
var count,offset;if(inRange(code_point,0x0080,0x07FF)){count=1;offset=0xC0;}else if(inRange(code_point,0x0800,0xFFFF)){count=2;offset=0xE0;}else if(inRange(code_point,0x10000,0x10FFFF)){count=3;offset=0xF0;}
var result=output_byte_stream.emit(div(code_point,Math.pow(64,count))+offset);while(count>0){var temp=div(code_point,Math.pow(64,count-1));result=output_byte_stream.emit(0x80+(temp%64));count-=1;}
return result;};}
name_to_encoding['utf-8'].getEncoder=function(options){return new UTF8Encoder(options);};name_to_encoding['utf-8'].getDecoder=function(options){return new UTF8Decoder(options);};function SingleByteDecoder(index,options){var fatal=options.fatal;this.decode=function(byte_pointer){var bite=byte_pointer.get();if(bite===EOF_byte){return EOF_code_point;}
byte_pointer.offset(1);if(inRange(bite,0x00,0x7F)){return bite;}
var code_point=index[bite-0x80];if(code_point===null){return decoderError(fatal);}
return code_point;};}
function SingleByteEncoder(index,options){var fatal=options.fatal;this.encode=function(output_byte_stream,code_point_pointer){var code_point=code_point_pointer.get();if(code_point===EOF_code_point){return EOF_byte;}
code_point_pointer.offset(1);if(inRange(code_point,0x0000,0x007F)){return output_byte_stream.emit(code_point);}
var pointer=indexPointerFor(code_point,index);if(pointer===null){encoderError(code_point);}
return output_byte_stream.emit(pointer+0x80);};}
(function(){if(!('encoding-indexes'in global))
return;encodings.forEach(function(category){if(category['heading']!=='Legacy single-byte encodings')
return;category['encodings'].forEach(function(encoding){var idx=index(encoding['name']);encoding.getDecoder=function(options){return new SingleByteDecoder(idx,options);};encoding.getEncoder=function(options){return new SingleByteEncoder(idx,options);};});});}());function GB18030Decoder(options){var fatal=options.fatal;var gb18030_first=0x00,gb18030_second=0x00,gb18030_third=0x00;this.decode=function(byte_pointer){var bite=byte_pointer.get();if(bite===EOF_byte&&gb18030_first===0x00&&gb18030_second===0x00&&gb18030_third===0x00){return EOF_code_point;}
if(bite===EOF_byte&&(gb18030_first!==0x00||gb18030_second!==0x00||gb18030_third!==0x00)){gb18030_first=0x00;gb18030_second=0x00;gb18030_third=0x00;decoderError(fatal);}
byte_pointer.offset(1);var code_point;if(gb18030_third!==0x00){code_point=null;if(inRange(bite,0x30,0x39)){code_point=indexGB18030CodePointFor((((gb18030_first-0x81)*10+(gb18030_second-0x30))*126+
(gb18030_third-0x81))*10+bite-0x30);}
gb18030_first=0x00;gb18030_second=0x00;gb18030_third=0x00;if(code_point===null){byte_pointer.offset(-3);return decoderError(fatal);}
return code_point;}
if(gb18030_second!==0x00){if(inRange(bite,0x81,0xFE)){gb18030_third=bite;return null;}
byte_pointer.offset(-2);gb18030_first=0x00;gb18030_second=0x00;return decoderError(fatal);}
if(gb18030_first!==0x00){if(inRange(bite,0x30,0x39)){gb18030_second=bite;return null;}
var lead=gb18030_first;var pointer=null;gb18030_first=0x00;var offset=bite<0x7F?0x40:0x41;if(inRange(bite,0x40,0x7E)||inRange(bite,0x80,0xFE)){pointer=(lead-0x81)*190+(bite-offset);}
code_point=pointer===null?null:indexCodePointFor(pointer,index('gb18030'));if(pointer===null){byte_pointer.offset(-1);}
if(code_point===null){return decoderError(fatal);}
return code_point;}
if(inRange(bite,0x00,0x7F)){return bite;}
if(bite===0x80){return 0x20AC;}
if(inRange(bite,0x81,0xFE)){gb18030_first=bite;return null;}
return decoderError(fatal);};}
function GB18030Encoder(options){var fatal=options.fatal;this.encode=function(output_byte_stream,code_point_pointer){var code_point=code_point_pointer.get();if(code_point===EOF_code_point){return EOF_byte;}
code_point_pointer.offset(1);if(inRange(code_point,0x0000,0x007F)){return output_byte_stream.emit(code_point);}
var pointer=indexPointerFor(code_point,index('gb18030'));if(pointer!==null){var lead=div(pointer,190)+0x81;var trail=pointer%190;var offset=trail<0x3F?0x40:0x41;return output_byte_stream.emit(lead,trail+offset);}
pointer=indexGB18030PointerFor(code_point);var byte1=div(div(div(pointer,10),126),10);pointer=pointer-byte1*10*126*10;var byte2=div(div(pointer,10),126);pointer=pointer-byte2*10*126;var byte3=div(pointer,10);var byte4=pointer-byte3*10;return output_byte_stream.emit(byte1+0x81,byte2+0x30,byte3+0x81,byte4+0x30);};}
name_to_encoding['gb18030'].getEncoder=function(options){return new GB18030Encoder(options);};name_to_encoding['gb18030'].getDecoder=function(options){return new GB18030Decoder(options);};function HZGB2312Decoder(options){var fatal=options.fatal;var hzgb2312=false,hzgb2312_lead=0x00;this.decode=function(byte_pointer){var bite=byte_pointer.get();if(bite===EOF_byte&&hzgb2312_lead===0x00){return EOF_code_point;}
if(bite===EOF_byte&&hzgb2312_lead!==0x00){hzgb2312_lead=0x00;return decoderError(fatal);}
byte_pointer.offset(1);if(hzgb2312_lead===0x7E){hzgb2312_lead=0x00;if(bite===0x7B){hzgb2312=true;return null;}
if(bite===0x7D){hzgb2312=false;return null;}
if(bite===0x7E){return 0x007E;}
if(bite===0x0A){return null;}
byte_pointer.offset(-1);return decoderError(fatal);}
if(hzgb2312_lead!==0x00){var lead=hzgb2312_lead;hzgb2312_lead=0x00;var code_point=null;if(inRange(bite,0x21,0x7E)){code_point=indexCodePointFor((lead-1)*190+
(bite+0x3F),index('gb18030'));}
if(bite===0x0A){hzgb2312=false;}
if(code_point===null){return decoderError(fatal);}
return code_point;}
if(bite===0x7E){hzgb2312_lead=0x7E;return null;}
if(hzgb2312){if(inRange(bite,0x20,0x7F)){hzgb2312_lead=bite;return null;}
if(bite===0x0A){hzgb2312=false;}
return decoderError(fatal);}
if(inRange(bite,0x00,0x7F)){return bite;}
return decoderError(fatal);};}
function HZGB2312Encoder(options){var fatal=options.fatal;var hzgb2312=false;this.encode=function(output_byte_stream,code_point_pointer){var code_point=code_point_pointer.get();if(code_point===EOF_code_point){return EOF_byte;}
code_point_pointer.offset(1);if(inRange(code_point,0x0000,0x007F)&&hzgb2312){code_point_pointer.offset(-1);hzgb2312=false;return output_byte_stream.emit(0x7E,0x7D);}
if(code_point===0x007E){return output_byte_stream.emit(0x7E,0x7E);}
if(inRange(code_point,0x0000,0x007F)){return output_byte_stream.emit(code_point);}
if(!hzgb2312){code_point_pointer.offset(-1);hzgb2312=true;return output_byte_stream.emit(0x7E,0x7B);}
var pointer=indexPointerFor(code_point,index('gb18030'));if(pointer===null){return encoderError(code_point);}
var lead=div(pointer,190)+1;var trail=pointer%190-0x3F;if(!inRange(lead,0x21,0x7E)||!inRange(trail,0x21,0x7E)){return encoderError(code_point);}
return output_byte_stream.emit(lead,trail);};}
name_to_encoding['hz-gb-2312'].getEncoder=function(options){return new HZGB2312Encoder(options);};name_to_encoding['hz-gb-2312'].getDecoder=function(options){return new HZGB2312Decoder(options);};function Big5Decoder(options){var fatal=options.fatal;var big5_lead=0x00,big5_pending=null;this.decode=function(byte_pointer){if(big5_pending!==null){var pending=big5_pending;big5_pending=null;return pending;}
var bite=byte_pointer.get();if(bite===EOF_byte&&big5_lead===0x00){return EOF_code_point;}
if(bite===EOF_byte&&big5_lead!==0x00){big5_lead=0x00;return decoderError(fatal);}
byte_pointer.offset(1);if(big5_lead!==0x00){var lead=big5_lead;var pointer=null;big5_lead=0x00;var offset=bite<0x7F?0x40:0x62;if(inRange(bite,0x40,0x7E)||inRange(bite,0xA1,0xFE)){pointer=(lead-0x81)*157+(bite-offset);}
if(pointer===1133){big5_pending=0x0304;return 0x00CA;}
if(pointer===1135){big5_pending=0x030C;return 0x00CA;}
if(pointer===1164){big5_pending=0x0304;return 0x00EA;}
if(pointer===1166){big5_pending=0x030C;return 0x00EA;}
var code_point=(pointer===null)?null:indexCodePointFor(pointer,index('big5'));if(pointer===null){byte_pointer.offset(-1);}
if(code_point===null){return decoderError(fatal);}
return code_point;}
if(inRange(bite,0x00,0x7F)){return bite;}
if(inRange(bite,0x81,0xFE)){big5_lead=bite;return null;}
return decoderError(fatal);};}
function Big5Encoder(options){var fatal=options.fatal;this.encode=function(output_byte_stream,code_point_pointer){var code_point=code_point_pointer.get();if(code_point===EOF_code_point){return EOF_byte;}
code_point_pointer.offset(1);if(inRange(code_point,0x0000,0x007F)){return output_byte_stream.emit(code_point);}
var pointer=indexPointerFor(code_point,index('big5'));if(pointer===null){return encoderError(code_point);}
var lead=div(pointer,157)+0x81;var trail=pointer%157;var offset=trail<0x3F?0x40:0x62;return output_byte_stream.emit(lead,trail+offset);};}
name_to_encoding['big5'].getEncoder=function(options){return new Big5Encoder(options);};name_to_encoding['big5'].getDecoder=function(options){return new Big5Decoder(options);};function EUCJPDecoder(options){var fatal=options.fatal;var eucjp_first=0x00,eucjp_second=0x00;this.decode=function(byte_pointer){var bite=byte_pointer.get();if(bite===EOF_byte){if(eucjp_first===0x00&&eucjp_second===0x00){return EOF_code_point;}
eucjp_first=0x00;eucjp_second=0x00;return decoderError(fatal);}
byte_pointer.offset(1);var lead,code_point;if(eucjp_second!==0x00){lead=eucjp_second;eucjp_second=0x00;code_point=null;if(inRange(lead,0xA1,0xFE)&&inRange(bite,0xA1,0xFE)){code_point=indexCodePointFor((lead-0xA1)*94+bite-0xA1,index('jis0212'));}
if(!inRange(bite,0xA1,0xFE)){byte_pointer.offset(-1);}
if(code_point===null){return decoderError(fatal);}
return code_point;}
if(eucjp_first===0x8E&&inRange(bite,0xA1,0xDF)){eucjp_first=0x00;return 0xFF61+bite-0xA1;}
if(eucjp_first===0x8F&&inRange(bite,0xA1,0xFE)){eucjp_first=0x00;eucjp_second=bite;return null;}
if(eucjp_first!==0x00){lead=eucjp_first;eucjp_first=0x00;code_point=null;if(inRange(lead,0xA1,0xFE)&&inRange(bite,0xA1,0xFE)){code_point=indexCodePointFor((lead-0xA1)*94+bite-0xA1,index('jis0208'));}
if(!inRange(bite,0xA1,0xFE)){byte_pointer.offset(-1);}
if(code_point===null){return decoderError(fatal);}
return code_point;}
if(inRange(bite,0x00,0x7F)){return bite;}
if(bite===0x8E||bite===0x8F||(inRange(bite,0xA1,0xFE))){eucjp_first=bite;return null;}
return decoderError(fatal);};}
function EUCJPEncoder(options){var fatal=options.fatal;this.encode=function(output_byte_stream,code_point_pointer){var code_point=code_point_pointer.get();if(code_point===EOF_code_point){return EOF_byte;}
code_point_pointer.offset(1);if(inRange(code_point,0x0000,0x007F)){return output_byte_stream.emit(code_point);}
if(code_point===0x00A5){return output_byte_stream.emit(0x5C);}
if(code_point===0x203E){return output_byte_stream.emit(0x7E);}
if(inRange(code_point,0xFF61,0xFF9F)){return output_byte_stream.emit(0x8E,code_point-0xFF61+0xA1);}
var pointer=indexPointerFor(code_point,index('jis0208'));if(pointer===null){return encoderError(code_point);}
var lead=div(pointer,94)+0xA1;var trail=pointer%94+0xA1;return output_byte_stream.emit(lead,trail);};}
name_to_encoding['euc-jp'].getEncoder=function(options){return new EUCJPEncoder(options);};name_to_encoding['euc-jp'].getDecoder=function(options){return new EUCJPDecoder(options);};function ISO2022JPDecoder(options){var fatal=options.fatal;var state={ASCII:0,escape_start:1,escape_middle:2,escape_final:3,lead:4,trail:5,Katakana:6};var iso2022jp_state=state.ASCII,iso2022jp_jis0212=false,iso2022jp_lead=0x00;this.decode=function(byte_pointer){var bite=byte_pointer.get();if(bite!==EOF_byte){byte_pointer.offset(1);}
switch(iso2022jp_state){default:case state.ASCII:if(bite===0x1B){iso2022jp_state=state.escape_start;return null;}
if(inRange(bite,0x00,0x7F)){return bite;}
if(bite===EOF_byte){return EOF_code_point;}
return decoderError(fatal);case state.escape_start:if(bite===0x24||bite===0x28){iso2022jp_lead=bite;iso2022jp_state=state.escape_middle;return null;}
if(bite!==EOF_byte){byte_pointer.offset(-1);}
iso2022jp_state=state.ASCII;return decoderError(fatal);case state.escape_middle:var lead=iso2022jp_lead;iso2022jp_lead=0x00;if(lead===0x24&&(bite===0x40||bite===0x42)){iso2022jp_jis0212=false;iso2022jp_state=state.lead;return null;}
if(lead===0x24&&bite===0x28){iso2022jp_state=state.escape_final;return null;}
if(lead===0x28&&(bite===0x42||bite===0x4A)){iso2022jp_state=state.ASCII;return null;}
if(lead===0x28&&bite===0x49){iso2022jp_state=state.Katakana;return null;}
if(bite===EOF_byte){byte_pointer.offset(-1);}else{byte_pointer.offset(-2);}
iso2022jp_state=state.ASCII;return decoderError(fatal);case state.escape_final:if(bite===0x44){iso2022jp_jis0212=true;iso2022jp_state=state.lead;return null;}
if(bite===EOF_byte){byte_pointer.offset(-2);}else{byte_pointer.offset(-3);}
iso2022jp_state=state.ASCII;return decoderError(fatal);case state.lead:if(bite===0x0A){iso2022jp_state=state.ASCII;return decoderError(fatal,0x000A);}
if(bite===0x1B){iso2022jp_state=state.escape_start;return null;}
if(bite===EOF_byte){return EOF_code_point;}
iso2022jp_lead=bite;iso2022jp_state=state.trail;return null;case state.trail:iso2022jp_state=state.lead;if(bite===EOF_byte){return decoderError(fatal);}
var code_point=null;var pointer=(iso2022jp_lead-0x21)*94+bite-0x21;if(inRange(iso2022jp_lead,0x21,0x7E)&&inRange(bite,0x21,0x7E)){code_point=(iso2022jp_jis0212===false)?indexCodePointFor(pointer,index('jis0208')):indexCodePointFor(pointer,index('jis0212'));}
if(code_point===null){return decoderError(fatal);}
return code_point;case state.Katakana:if(bite===0x1B){iso2022jp_state=state.escape_start;return null;}
if(inRange(bite,0x21,0x5F)){return 0xFF61+bite-0x21;}
if(bite===EOF_byte){return EOF_code_point;}
return decoderError(fatal);}};}
function ISO2022JPEncoder(options){var fatal=options.fatal;var state={ASCII:0,lead:1,Katakana:2};var iso2022jp_state=state.ASCII;this.encode=function(output_byte_stream,code_point_pointer){var code_point=code_point_pointer.get();if(code_point===EOF_code_point){return EOF_byte;}
code_point_pointer.offset(1);if((inRange(code_point,0x0000,0x007F)||code_point===0x00A5||code_point===0x203E)&&iso2022jp_state!==state.ASCII){code_point_pointer.offset(-1);iso2022jp_state=state.ASCII;return output_byte_stream.emit(0x1B,0x28,0x42);}
if(inRange(code_point,0x0000,0x007F)){return output_byte_stream.emit(code_point);}
if(code_point===0x00A5){return output_byte_stream.emit(0x5C);}
if(code_point===0x203E){return output_byte_stream.emit(0x7E);}
if(inRange(code_point,0xFF61,0xFF9F)&&iso2022jp_state!==state.Katakana){code_point_pointer.offset(-1);iso2022jp_state=state.Katakana;return output_byte_stream.emit(0x1B,0x28,0x49);}
if(inRange(code_point,0xFF61,0xFF9F)){return output_byte_stream.emit(code_point-0xFF61-0x21);}
if(iso2022jp_state!==state.lead){code_point_pointer.offset(-1);iso2022jp_state=state.lead;return output_byte_stream.emit(0x1B,0x24,0x42);}
var pointer=indexPointerFor(code_point,index('jis0208'));if(pointer===null){return encoderError(code_point);}
var lead=div(pointer,94)+0x21;var trail=pointer%94+0x21;return output_byte_stream.emit(lead,trail);};}
name_to_encoding['iso-2022-jp'].getEncoder=function(options){return new ISO2022JPEncoder(options);};name_to_encoding['iso-2022-jp'].getDecoder=function(options){return new ISO2022JPDecoder(options);};function ShiftJISDecoder(options){var fatal=options.fatal;var shiftjis_lead=0x00;this.decode=function(byte_pointer){var bite=byte_pointer.get();if(bite===EOF_byte&&shiftjis_lead===0x00){return EOF_code_point;}
if(bite===EOF_byte&&shiftjis_lead!==0x00){shiftjis_lead=0x00;return decoderError(fatal);}
byte_pointer.offset(1);if(shiftjis_lead!==0x00){var lead=shiftjis_lead;shiftjis_lead=0x00;if(inRange(bite,0x40,0x7E)||inRange(bite,0x80,0xFC)){var offset=(bite<0x7F)?0x40:0x41;var lead_offset=(lead<0xA0)?0x81:0xC1;var code_point=indexCodePointFor((lead-lead_offset)*188+
bite-offset,index('jis0208'));if(code_point===null){return decoderError(fatal);}
return code_point;}
byte_pointer.offset(-1);return decoderError(fatal);}
if(inRange(bite,0x00,0x80)){return bite;}
if(inRange(bite,0xA1,0xDF)){return 0xFF61+bite-0xA1;}
if(inRange(bite,0x81,0x9F)||inRange(bite,0xE0,0xFC)){shiftjis_lead=bite;return null;}
return decoderError(fatal);};}
function ShiftJISEncoder(options){var fatal=options.fatal;this.encode=function(output_byte_stream,code_point_pointer){var code_point=code_point_pointer.get();if(code_point===EOF_code_point){return EOF_byte;}
code_point_pointer.offset(1);if(inRange(code_point,0x0000,0x0080)){return output_byte_stream.emit(code_point);}
if(code_point===0x00A5){return output_byte_stream.emit(0x5C);}
if(code_point===0x203E){return output_byte_stream.emit(0x7E);}
if(inRange(code_point,0xFF61,0xFF9F)){return output_byte_stream.emit(code_point-0xFF61+0xA1);}
var pointer=indexPointerFor(code_point,index('jis0208'));if(pointer===null){return encoderError(code_point);}
var lead=div(pointer,188);var lead_offset=lead<0x1F?0x81:0xC1;var trail=pointer%188;var offset=trail<0x3F?0x40:0x41;return output_byte_stream.emit(lead+lead_offset,trail+offset);};}
name_to_encoding['shift_jis'].getEncoder=function(options){return new ShiftJISEncoder(options);};name_to_encoding['shift_jis'].getDecoder=function(options){return new ShiftJISDecoder(options);};function EUCKRDecoder(options){var fatal=options.fatal;var euckr_lead=0x00;this.decode=function(byte_pointer){var bite=byte_pointer.get();if(bite===EOF_byte&&euckr_lead===0){return EOF_code_point;}
if(bite===EOF_byte&&euckr_lead!==0){euckr_lead=0x00;return decoderError(fatal);}
byte_pointer.offset(1);if(euckr_lead!==0x00){var lead=euckr_lead;var pointer=null;euckr_lead=0x00;if(inRange(lead,0x81,0xC6)){var temp=(26+26+126)*(lead-0x81);if(inRange(bite,0x41,0x5A)){pointer=temp+bite-0x41;}else if(inRange(bite,0x61,0x7A)){pointer=temp+26+bite-0x61;}else if(inRange(bite,0x81,0xFE)){pointer=temp+26+26+bite-0x81;}}
if(inRange(lead,0xC7,0xFD)&&inRange(bite,0xA1,0xFE)){pointer=(26+26+126)*(0xC7-0x81)+(lead-0xC7)*94+
(bite-0xA1);}
var code_point=(pointer===null)?null:indexCodePointFor(pointer,index('euc-kr'));if(pointer===null){byte_pointer.offset(-1);}
if(code_point===null){return decoderError(fatal);}
return code_point;}
if(inRange(bite,0x00,0x7F)){return bite;}
if(inRange(bite,0x81,0xFD)){euckr_lead=bite;return null;}
return decoderError(fatal);};}
function EUCKREncoder(options){var fatal=options.fatal;this.encode=function(output_byte_stream,code_point_pointer){var code_point=code_point_pointer.get();if(code_point===EOF_code_point){return EOF_byte;}
code_point_pointer.offset(1);if(inRange(code_point,0x0000,0x007F)){return output_byte_stream.emit(code_point);}
var pointer=indexPointerFor(code_point,index('euc-kr'));if(pointer===null){return encoderError(code_point);}
var lead,trail;if(pointer<((26+26+126)*(0xC7-0x81))){lead=div(pointer,(26+26+126))+0x81;trail=pointer%(26+26+126);var offset=trail<26?0x41:trail<26+26?0x47:0x4D;return output_byte_stream.emit(lead,trail+offset);}
pointer=pointer-(26+26+126)*(0xC7-0x81);lead=div(pointer,94)+0xC7;trail=pointer%94+0xA1;return output_byte_stream.emit(lead,trail);};}
name_to_encoding['euc-kr'].getEncoder=function(options){return new EUCKREncoder(options);};name_to_encoding['euc-kr'].getDecoder=function(options){return new EUCKRDecoder(options);};function UTF16Decoder(utf16_be,options){var fatal=options.fatal;var utf16_lead_byte=null,utf16_lead_surrogate=null;this.decode=function(byte_pointer){var bite=byte_pointer.get();if(bite===EOF_byte&&utf16_lead_byte===null&&utf16_lead_surrogate===null){return EOF_code_point;}
if(bite===EOF_byte&&(utf16_lead_byte!==null||utf16_lead_surrogate!==null)){return decoderError(fatal);}
byte_pointer.offset(1);if(utf16_lead_byte===null){utf16_lead_byte=bite;return null;}
var code_point;if(utf16_be){code_point=(utf16_lead_byte<<8)+bite;}else{code_point=(bite<<8)+utf16_lead_byte;}
utf16_lead_byte=null;if(utf16_lead_surrogate!==null){var lead_surrogate=utf16_lead_surrogate;utf16_lead_surrogate=null;if(inRange(code_point,0xDC00,0xDFFF)){return 0x10000+(lead_surrogate-0xD800)*0x400+
(code_point-0xDC00);}
byte_pointer.offset(-2);return decoderError(fatal);}
if(inRange(code_point,0xD800,0xDBFF)){utf16_lead_surrogate=code_point;return null;}
if(inRange(code_point,0xDC00,0xDFFF)){return decoderError(fatal);}
return code_point;};}
function UTF16Encoder(utf16_be,options){var fatal=options.fatal;this.encode=function(output_byte_stream,code_point_pointer){function convert_to_bytes(code_unit){var byte1=code_unit>>8;var byte2=code_unit&0x00FF;if(utf16_be){return output_byte_stream.emit(byte1,byte2);}
return output_byte_stream.emit(byte2,byte1);}
var code_point=code_point_pointer.get();if(code_point===EOF_code_point){return EOF_byte;}
code_point_pointer.offset(1);if(inRange(code_point,0xD800,0xDFFF)){encoderError(code_point);}
if(code_point<=0xFFFF){return convert_to_bytes(code_point);}
var lead=div((code_point-0x10000),0x400)+0xD800;var trail=((code_point-0x10000)%0x400)+0xDC00;convert_to_bytes(lead);return convert_to_bytes(trail);};}
name_to_encoding['utf-16be'].getEncoder=function(options){return new UTF16Encoder(true,options);};name_to_encoding['utf-16be'].getDecoder=function(options){return new UTF16Decoder(true,options);};name_to_encoding['utf-16le'].getEncoder=function(options){return new UTF16Encoder(false,options);};name_to_encoding['utf-16le'].getDecoder=function(options){return new UTF16Decoder(false,options);};function XUserDefinedDecoder(options){var fatal=options.fatal;this.decode=function(byte_pointer){var bite=byte_pointer.get();if(bite===EOF_byte){return EOF_code_point;}
byte_pointer.offset(1);if(inRange(bite,0x00,0x7F)){return bite;}
return 0xF780+bite-0x80;};}
function XUserDefinedEncoder(index,options){var fatal=options.fatal;this.encode=function(output_byte_stream,code_point_pointer){var code_point=code_point_pointer.get();if(code_point===EOF_code_point){return EOF_byte;}
code_point_pointer.offset(1);if(inRange(code_point,0x0000,0x007F)){return output_byte_stream.emit(code_point);}
if(inRange(code_point,0xF780,0xF7FF)){return output_byte_stream.emit(code_point-0xF780+0x80);}
encoderError(code_point);};}
name_to_encoding['x-user-defined'].getEncoder=function(options){return new XUserDefinedEncoder(false,options);};name_to_encoding['x-user-defined'].getDecoder=function(options){return new XUserDefinedDecoder(false,options);};function detectEncoding(label,input_stream){if(input_stream.match([0xFF,0xFE])){input_stream.offset(2);return 'utf-16le';}
if(input_stream.match([0xFE,0xFF])){input_stream.offset(2);return 'utf-16be';}
if(input_stream.match([0xEF,0xBB,0xBF])){input_stream.offset(3);return 'utf-8';}
return label;}
if(!('TextEncoder'in global))global['TextEncoder']=TextEncoder;if(!('TextDecoder'in global))global['TextDecoder']=TextDecoder;}(this));