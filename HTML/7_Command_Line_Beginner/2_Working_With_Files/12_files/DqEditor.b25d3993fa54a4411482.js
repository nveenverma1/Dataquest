(window.webpackJsonp=window.webpackJsonp||[]).push([[40],{709:function(e,t,o){"use strict";o.r(t);var r=o(0),n=o.n(r),a=o(1),i=o.n(a),s=o(2),l=o.n(s),c=(o(860),o(8)),u=o.n(c),p=o(360),d=o.n(p);o(858);o(855),o(854);o.d(t,"DqEditor",function(){return v});var _=Object.assign||function(e){for(var t=1;t<arguments.length;t++){var o=arguments[t];for(var r in o)Object.prototype.hasOwnProperty.call(o,r)&&(e[r]=o[r])}return e},f=function(){function e(e,t){for(var o=0;o<t.length;o++){var r=t[o];r.enumerable=r.enumerable||!1,r.configurable=!0,"value"in r&&(r.writable=!0),Object.defineProperty(e,r.key,r)}}return function(t,o,r){return o&&e(t.prototype,o),r&&e(t,r),t}}();function m(e,t){if(!e)throw new ReferenceError("this hasn't been initialised - super() hasn't been called");return!t||"object"!=typeof t&&"function"!=typeof t?e:t}o(866),o(864),o(862),o(857);var h=/[a-zA-Z_$][\w_$]*/,g=function(e){for(var t=arguments.length>1&&void 0!==arguments[1]?arguments[1]:{},o=void 0,r=[],n=new RegExp(h,"g");o=n.exec(e);)t[o[0]]||(t[o[0]]=!0,r.push(o[0]));return r},y=function(e){for(var t=e.getCursor(),o=e.getLine(t.line),r=t.ch,n=r;n>0&&h.test(o.charAt(n-1));)--n;return n!==r&&o.slice(n,r)},b=2,v=function(e){function t(){var e,o,r;!function(e,t){if(!(e instanceof t))throw new TypeError("Cannot call a class as a function")}(this,t);for(var n=arguments.length,a=Array(n),i=0;i<n;i++)a[i]=arguments[i];return o=r=m(this,(e=t.__proto__||Object.getPrototypeOf(t)).call.apply(e,[this].concat(a))),r.state={modes_loaded:{},options:{}},r.return_mode=function(){return r.state.modes_loaded[r.props.mode]||"python"},r.check_if_autocomplete=function(e,t){t.key.length>1||!e.state.completionActive&&/[a-zA-Z_."']/.test(t.key)&&r.props.codemirror.commands.autocomplete(e,null,{completeSingle:!1,generalKey:!0})},r.get_words=function(e){var t=[],o=e.getHelper(e.getCursor(),"hintWords");o&&(t=o);var n=t.reduce(function(e,t){return e[t]=!0,e},{});return(t=(t=t.concat(g(r.props.value,n))).concat(g(r.props.autocomplete_extra_text,n))).sort(),t},r.autocomplete=function(e,t){var o=r.get_words(e),n=e.getCursor();if(!t.generalKey)return{list:o,from:n,to:n};var a=y(e);if(a&&!(a.length<b)){l.a.pull(o,a);var i=a.toLowerCase();return{list:o.filter(function(e){return l.a.startsWith(e.toLowerCase(),i)}),from:r.props.codemirror.Pos(n.line,n.ch-a.length),to:n}}},r.set_mode_loaded=function(e,t){r._still_mounted&&(r.setState({modes_loaded:_({},r.state.modes_loaded,function(e,t,o){return t in e?Object.defineProperty(e,t,{value:o,enumerable:!0,configurable:!0,writable:!0}):e[t]=o,e}({},e,t))}),r.set_options(r.props,t))},r.handle_value_change=function(e,t){null!=r.props.onChange&&"setValue"!==t.origin&&r.props.onChange(e.getValue())},r.set_text_area_ref=function(e){r._textarea_ref=e},m(r,o)}return function(e,t){if("function"!=typeof t&&null!==t)throw new TypeError("Super expression must either be null or a function, not "+typeof t);e.prototype=Object.create(t&&t.prototype,{constructor:{value:e,enumerable:!1,writable:!0,configurable:!0}}),t&&(Object.setPrototypeOf?Object.setPrototypeOf(e,t):e.__proto__=t)}(t,n.a.PureComponent),f(t,[{key:"componentWillMount",value:function(){this._still_mounted=!0,this.set_options(),this.props.load_mode(this.props.mode,this.set_mode_loaded)}},{key:"componentDidMount",value:function(){var e=this,t=navigator.userAgent.toLowerCase().indexOf("firefox")>-1?100:0;setTimeout(function(){null!=e._textarea_ref&&null!=e._still_mounted&&(e._codemirror_ref=e.props.codemirror.fromTextArea(e._textarea_ref,e.state.options),e._codemirror_ref.on("change",e.handle_value_change),e._codemirror_ref.setValue(e.props.value),e.props.extra_codemirror_setup&&e.props.extra_codemirror_setup(e._codemirror_ref),!e.props.readOnly&&e.props.autocomplete&&e._codemirror_ref.on("keyup",e.check_if_autocomplete))},t)}},{key:"componentWillReceiveProps",value:function(e){var t=["onDark","mode","wrapLines","readOnly","lineNumbers","extra_codemirror_options"];l.a.isEqual(l.a.pick(e,t),l.a.pick(this.props,t))||this.set_options(e),this._codemirror_ref&&e.value!==this._codemirror_ref.getValue()&&this._codemirror_ref.setValue(e.value)}},{key:"componentWillUnmount",value:function(){this._codemirror_ref&&this._codemirror_ref.toTextArea(),delete this._still_mounted}},{key:"tab_mapping",value:function(e){e.somethingSelected()?e.indentSelection("add"):e.execCommand("insertSoftTab")}},{key:"shift_tab_mapping",value:function(e){e.indentSelection("subtract")}},{key:"set_options",value:function(){var e=arguments.length>0&&void 0!==arguments[0]?arguments[0]:this.props,t=arguments.length>1&&void 0!==arguments[1]?arguments[1]:this.return_mode(),o=u()(_({lineWrapping:e.wrapLines,mode:t,theme:e.onDark?"dq-dark":"dq-light",cursorBlinkRate:e.readOnly?-1:530},l.a.pick(e,["readOnly"]),{lineNumbers:e.lineNumbers,indentUnit:4,extraKeys:{Tab:this.tab_mapping,"Shift-Tab":this.shift_tab_mapping,"Ctrl-Space":e.readOnly?"":"autocomplete"},hintOptions:{hint:this.autocomplete}})).merge(this.props.extra_codemirror_options,{deep:!0});this.setState({options:o}),this.apply_options(o)}},{key:"apply_options",value:function(e){var t=this;null!=this._codemirror_ref&&l.a.forEach(e,function(e,o){var r=t._codemirror_ref.getOption(o);l.a.isEqual(r,e)||t._codemirror_ref.setOption(o,e)})}},{key:"render",value:function(){return n.a.createElement("div",{className:"dq_theme "+l.a.defaultTo(this.props.className,"")+" DqEditor__root"},n.a.createElement("textarea",{ref:this.set_text_area_ref,defaultValue:this.props.value,autoComplete:"off"}))}}]),t}();v.propTypes={onChange:i.a.func,value:i.a.string,className:i.a.string,extra_codemirror_setup:i.a.func,autocomplete_extra_text:i.a.string,onDark:i.a.bool,mode:i.a.string,wrapLines:i.a.bool,readOnly:i.a.bool,lineNumbers:i.a.bool,extra_codemirror_options:i.a.object,autocomplete:i.a.bool,load_mode:i.a.func.isRequired,codemirror:i.a.any.isRequired},v.defaultProps={value:"",onDark:!1,mode:"python",wrapLines:!0,readOnly:!1,lineNumbers:!0,extra_codemirror_options:{},autocomplete_extra_text:"",load_mode:function(e,t){switch(e.toLowerCase()){case"r":o.e(30).then(function(){o(1459),t(e,"r")}.bind(null,o)).catch(o.oe);break;case"sql":o.e(20).then(function(){o(1458),t(e,"text/x-sql")}.bind(null,o)).catch(o.oe);break;case"regex":o.e(29).then(function(){o(1457),t(e,"text/x-regex")}.bind(null,o)).catch(o.oe);break;case"text":t(e,"text/plain");break;case"":case"python":case"python 3":t(e,"python");break;default:console.warn('Falling back to Python. Mode tried was "'+e+'"'),t(e,"python")}},codemirror:d.a,autocomplete:!0},v.displayName="DqEditor";t.default=v},860:function(e,t,o){e.exports={root:"DqEditor__root"}},862:function(e,t,o){},864:function(e,t,o){}}]);
//# sourceMappingURL=DqEditor.b25d3993fa54a4411482.js.map