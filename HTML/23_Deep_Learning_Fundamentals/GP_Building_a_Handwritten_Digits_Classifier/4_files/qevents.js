!function(t){function r(n){if(e[n])return e[n].exports;var i=e[n]={i:n,l:!1,exports:{}};return t[n].call(i.exports,i,i.exports,r),i.l=!0,i.exports}var e={};r.m=t,r.c=e,r.d=function(t,e,n){r.o(t,e)||Object.defineProperty(t,e,{configurable:!1,enumerable:!0,get:n})},r.n=function(t){var e=t&&t.__esModule?function(){return t["default"]}:function(){return t};return r.d(e,"a",e),e},r.o=function(t,r){return Object.prototype.hasOwnProperty.call(t,r)},r.p="",r(r.s="./shared/qevents/main.js")}({"./shared/Class.js":function(t,r){function e(t,r){function e(){if(i||(t.call(u),n(l,r,s),i=!0,r=null),this!==u){var e=this.__init__;e&&e.apply(this,arguments)}}var i,s=a.prototype=t.prototype,l=new a;return e.prototype=l,e.extend=o,l.constructor=e,e}function n(t,r,e){for(var n in r)r.hasOwnProperty(n)&&(t[n]=e?i(n,r,e):r[n])}function i(t,r,e){var n=r[t],i=e[t];return"function"==typeof n&&"function"==typeof i&&n!==i&&s.test(n)?function(){var r=this._super;this._super=e[t];try{return n.apply(this,arguments)}finally{this._super=r}}:n}function o(t){return e(this,t)}var s=/xyz/.test(function(){xyz})?/\b_super\b/:/.*/,a=function(){},u={};r.Class=o.call(function(){},{})},"./shared/polyfills/array.js":function(t,r){var e=function(t,r,e){"function"==typeof Object.defineProperty?Object.defineProperty(t,r,{configurable:!0,value:e,writable:!0,enumerable:!1}):t[r]=e};if(!Array.prototype.every){var n=function(t,r){"use strict";var e,n;if(null===this)throw new TypeError("this is null or not defined");var i=Object(this),o=i.length>>>0;if("function"!=typeof t)throw new TypeError;for(arguments.length>1&&(e=r),n=0;n<o;){var s;if(n in i){s=i[n];if(!t.call(e,s,n,i))return!1}n++}return!0};e(Array.prototype,"every",n)}if(!Array.prototype.some){var i=function(t){"use strict";if(null===this)throw new TypeError("Array.prototype.some called on null or undefined");if("function"!=typeof t)throw new TypeError;for(var r=Object(this),e=r.length>>>0,n=arguments.length>=2?arguments[1]:void 0,i=0;i<e;i++)if(i in r&&t.call(n,r[i],i,r))return!0;return!1};e(Array.prototype,"some",i)}if(!Array.prototype.indexOf){var o=function(t,r){var e;if(null===this)throw new TypeError('"this" is null or not defined');var n=Object(this),i=n.length>>>0;if(0===i)return-1;var o=+r||0;if(Math.abs(o)===Infinity&&(o=0),o>=i)return-1;for(e=Math.max(o>=0?o:i-Math.abs(o),0);e<i;){if(e in n&&n[e]===t)return e;e++}return-1};e(Array.prototype,"indexOf",o)}if(!Array.prototype.forEach){var s=function(t,r){var e,n;if(null===this)throw new TypeError(" this is null or not defined");var i=Object(this),o=i.length>>>0;if("function"!=typeof t)throw new TypeError(t+" is not a function");for(arguments.length>1&&(e=r),n=0;n<o;){var s;n in i&&(s=i[n],t.call(e,s,n,i)),n++}};e(Array.prototype,"forEach",s)}if(!Array.prototype.map){var a=function(t,r){var e,n,i;if(null===this)throw new TypeError(" this is null or not defined");var o=Object(this),s=o.length>>>0;if("function"!=typeof t)throw new TypeError(t+" is not a function");for(arguments.length>1&&(e=r),n=new Array(s),i=0;i<s;){var a,u;i in o&&(a=o[i],u=t.call(e,a,i,o),n[i]=u),i++}return n};e(Array.prototype,"map",a)}if(!Array.prototype.filter){var u=function(t){"use strict";if(void 0===this||null===this)throw new TypeError;var r=Object(this),e=r.length>>>0;if("function"!=typeof t)throw new TypeError;for(var n=[],i=arguments.length>=2?arguments[1]:void 0,o=0;o<e;o++)if(o in r){var s=r[o];t.call(i,s,o,r)&&n.push(s)}return n};e(Array.prototype,"filter",u)}if(!Array.prototype.reduce){var l=function(t){"use strict";if(null===this)throw new TypeError("Array.prototype.reduce called on null or undefined");if("function"!=typeof t)throw new TypeError(t+" is not a function");var r,e=Object(this),n=e.length>>>0,i=0;if(2==arguments.length)r=arguments[1];else{for(;i<n&&!(i in e);)i++;if(i>=n)throw new TypeError("Reduce of empty array with no initial value");r=e[i++]}for(;i<n;i++)i in e&&(r=t(r,e[i],i,e));return r};e(Array.prototype,"reduce",l)}if(!Array.prototype.lastIndexOf){var f=function(t){"use strict";if(void 0===this||null===this)throw new TypeError;var r,e,n=Object(this),i=n.length>>>0;if(0===i)return-1;for(r=i-1,arguments.length>1&&(r=Number(arguments[1]),r!=r?r=0:0!==r&&r!=1/0&&r!=-1/0&&(r=(r>0||-1)*Math.floor(Math.abs(r)))),e=r>=0?Math.min(r,i-1):i-Math.abs(r);e>=0;e--)if(e in n&&n[e]===t)return e;return-1};e(Array.prototype,"lastIndexOf",f)}if(!Array.prototype.includes){var c=function(t){"use strict";if(null==this)throw new TypeError("Array.prototype.includes called on null or undefined");var r=Object(this),e=parseInt(r.length,10)||0;if(0===e)return!1;var n,i=parseInt(arguments[1],10)||0;i>=0?n=i:(n=e+i)<0&&(n=0);for(var o;n<e;){if(o=r[n],t===o||t!==t&&o!==o)return!0;n++}return!1};e(Array.prototype,"includes",c)}},"./shared/polyfills/classList.js":function(t,r){!function(){function t(t){this.el=t;for(var r=t.className.replace(/^\s+|\s+$/g,"").split(/\s+/),e=0;e<r.length;e++)n.call(this,r[e])}function r(t,r,e){Object.defineProperty?Object.defineProperty(t,r,{get:e}):t.__defineGetter__(r,e)}if(!("undefined"==typeof window.Element||"classList"in document.documentElement)){var e=Array.prototype,n=e.push,i=e.splice,o=e.join;t.prototype={add:function(t){this.contains(t)||(n.call(this,t),this.el.className=this.toString())},contains:function(t){return-1!=this.el.className.indexOf(t)},item:function(t){return this[t]||null},remove:function(t){if(this.contains(t)){for(var r=0;r<this.length&&this[r]!=t;r++);i.call(this,r,1),this.el.className=this.toString()}},toString:function(){return o.call(this," ")},toggle:function(t){return this.contains(t)?this.remove(t):this.add(t),this.contains(t)}},window.DOMTokenList=t,r(Element.prototype,"classList",function(){return new t(this)})}}()},"./shared/polyfills/date.js":function(t,r){Date.now||(Date.now=function(){return(new Date).getTime()})},"./shared/polyfills/function.js":function(t,r){Function.prototype.bind||(Function.prototype.bind=function(t){if("function"!=typeof this)throw new TypeError("Function.prototype.bind - what is trying to be bound is not callable");var r=Array.prototype.slice.call(arguments,1),e=this,n=function(){},i=function(){return e.apply(this instanceof n?this:t,r.concat(Array.prototype.slice.call(arguments)))};return this.prototype&&(n.prototype=this.prototype),i.prototype=new n,i})},"./shared/polyfills/object.js":function(t,r){Object.keys||(Object.keys=function(){"use strict";var t=Object.prototype.hasOwnProperty,r=!{toString:null}.propertyIsEnumerable("toString"),e=["toString","toLocaleString","valueOf","hasOwnProperty","isPrototypeOf","propertyIsEnumerable","constructor"],n=e.length;return function(i){if("object"!=typeof i&&("function"!=typeof i||null===i))throw new TypeError("Object.keys called on non-object");var o,s,a=[];for(o in i)t.call(i,o)&&a.push(o);if(r)for(s=0;s<n;s++)t.call(i,e[s])&&a.push(e[s]);return a}}())},"./shared/polyfills/requestAnimationFrame.js":function(t,r){!function(){for(var t=0,r=["webkit","moz"],e=0;e<r.length&&!window.requestAnimationFrame;++e)window.requestAnimationFrame=window[r[e]+"RequestAnimationFrame"],window.cancelAnimationFrame=window[r[e]+"CancelAnimationFrame"]||window[r[e]+"CancelRequestAnimationFrame"];window.requestAnimationFrame||(window.requestAnimationFrame=function(r,e){var n=(new Date).getTime(),i=Math.max(0,16-(n-t)),o=window.setTimeout(function(){r(n+i)},i);return t=n+i,o}),window.cancelAnimationFrame||(window.cancelAnimationFrame=function(t){clearTimeout(t)})}()},"./shared/polyfills/string.js":function(t,r){String.prototype.endsWith||(String.prototype.endsWith=function(t,r){var e=this.toString();("number"!=typeof r||!isFinite(r)||Math.floor(r)!==r||r>e.length)&&(r=e.length),r-=t.length;var n=e.indexOf(t,r);return-1!==n&&n===r}),String.prototype.startsWith||(String.prototype.startsWith=function(t,r){return r=r||0,this.substr(r,t.length)===t}),String.prototype.trim||(String.prototype.trim=function(){return this.replace(/^[\s\uFEFF\xA0]+|[\s\uFEFF\xA0]+$/g,"")}),String.prototype.includes||(String.prototype.includes=function(t,r){"use strict";return"number"!=typeof r&&(r=0),!(r+t.length>this.length)&&-1!==this.indexOf(t,r)})},"./shared/qevents/main.js":function(t,r,e){e("./shared/polyfills/requestAnimationFrame.js"),e("./shared/polyfills/string.js"),e("./shared/polyfills/classList.js"),e("./shared/polyfills/array.js"),e("./shared/polyfills/function.js"),e("./shared/polyfills/object.js"),e("./shared/polyfills/date.js"),e("./shared/qevents/pixel.js").init(),e("./shared/qevents/queue.js").flush()},"./shared/qevents/pixel.js":function(t,r,e){function n(){try{var t=o("ia_share_url");if(null!==t)return t}catch(t){}try{return ia_document!==undefined&&ia_document.shareURL}catch(t){return}}function i(t){var r,e=[];for(var n in t)r=t[n],s(n)&&a(r)&&e.push(n+"="+encodeURIComponent(r));return e.join("&")}function o(t){var r=null,e=[];return window.location.search.substr(1).split("&").forEach(function(n){e=n.split("="),e[0]===t&&(r=decodeURIComponent(e[1]))}),r}function s(t){return"string"==typeof t}function a(t){return"string"==typeof t||!isNaN(Number(t))}function u(){function t(t,r){var e=window.history[t];window.history[t]=function(){var t=e.apply(this,arguments);return r.apply(this,arguments),t}}window.history.pushState&&window.history.replaceState&&(t("pushState",l),t("replaceState",l),window.addEventListener("popstate",l,!1))}function l(){!0!==window.qp.disablePushState&&r.quoraPixelHelper("track","ViewContent")}var f,c=e("./shared/Class.js").Class,p=c.extend({__init__:function(t){if("string"!=typeof t)throw new Error("Quora Pixel Error: The second argument passed to qp is invalid.");this.uuid=t,this.lastViewContentUrl=""},track:function(t,e){if("string"!=typeof t)throw new Error("Quora Pixel Error: The second argument passed to qp is invalid.");var n,i,o=this._getIsFBIAUrl(),s=this._getValueFromPassback(e),a=this._getUrl();this._shouldTrack(t,a)&&(n=this._getMetadata(t,a,o,s),i=this._getPixelUrl(n),r.firePixel(i))},_shouldTrack:function(t,r){return("ViewContent"!=t||r!=this.lastViewContentUrl)&&("ViewContent"==t&&(this.lastViewContentUrl=r),!0)},_getMetadata:function(t,r,e,n){var i={j:1,u:r,tag:t,ts:(new Date).getTime()};return e&&(i.fbia=1),n!==undefined&&(i.v=n),i},_getValueFromPassback:function(t){var r;if(t!==undefined&&null!==t&&t.value!==undefined&&"number"!=typeof(r=t.value)&&"string"!=typeof r)throw new Error("Quora Pixel Error: The third argument passed to qp is invalid.");return r},_getUrl:function(){var t=n();return t||(t=window.location.href),t},_getIsFBIAUrl:function(){return Boolean(n())},_getPixelUrl:function(t){return this._getBasePixelUrl()+this.uuid+"/pixel?"+i(t)},_getBasePixelUrl:function(){return"https://q.quora.com/_/ad/"}}),h=c.extend({__init__:function(){this.uuidToPixel={}},installPixel:function(t){if(this.uuidToPixel[t]===undefined){var r=new p(t);this.uuidToPixel[t]=r}},track:function(t,r){var e=Object.keys(this.uuidToPixel);if(!e.length)throw new Error("Quora Pixel Error: Base pixel code is not installed properly.");for(var n=0;n<e.length;n++){var i=e[n];this.uuidToPixel[i].track(t,r)}}});r.quoraPixelHelper=function(t,r,e){if("string"!=typeof arguments[0])throw new Error("Quora Pixel Error: The first argument passed to qp is invalid.");"init"==t?f.installPixel(r):"track"==t&&f.track(r,e)},r.firePixel=function(t){(new Image).src=t},r.init=function(){if(!window.qp)throw new Error("Quora Pixel Error: Base pixel code is not installed properly.");window.qp.qp=r.quoraPixelHelper,u(),f=new h},r.initializeStates=function(){f=new h}},"./shared/qevents/queue.js":function(t,r){r.flush=function(){var t,r=window.qp;for(r.queue||(r.queue=[]);r.queue.length;)t=r.queue.shift(),r.apply(r,t)}}});