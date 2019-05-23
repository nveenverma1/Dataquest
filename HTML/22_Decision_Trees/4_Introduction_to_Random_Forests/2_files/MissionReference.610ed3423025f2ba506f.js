(window.webpackJsonp=window.webpackJsonp||[]).push([[29],{1324:function(e,t,n){e.exports={title:"ReferenceItem__title",description:"ReferenceItem__description",matched:"ReferenceItem__matched",time:"ReferenceItem__time",root:"ReferenceItem__root",childBox:"ReferenceItem__childBox",text:"ReferenceItem__text",matched_list:"ReferenceItem__matched_list",new:"ReferenceItem__new",icon:"ReferenceItem__icon"}},1326:function(e,t,n){e.exports={input:"DqSearchBox__input",root:"DqSearchBox__root",clear:"DqSearchBox__clear"}},1328:function(e,t,n){e.exports={search_message:"MissionReference__search_message",searching:"MissionReference__searching",root:"MissionReference__root",content:"MissionReference__content",takeaways:"MissionReference__takeaways",takeaway_text:"MissionReference__takeaway_text",takeaways_header:"MissionReference__takeaways_header",search:"MissionReference__search",missions:"MissionReference__missions"}},1584:function(e,t,n){"use strict";n.r(t);var r={};n.r(r),n.d(r,"get_takeaways",function(){return te}),n.d(r,"search_update",function(){return ne});var a=n(0),s=n.n(a),i=n(1),o=n.n(i),c=n(6),l=n(3),u=(n(1328),n(1210)),_=(n(1326),n(20)),p=function(){function e(e,t){for(var n=0;n<t.length;n++){var r=t[n];r.enumerable=r.enumerable||!1,r.configurable=!0,"value"in r&&(r.writable=!0),Object.defineProperty(e,r.key,r)}}return function(t,n,r){return n&&e(t.prototype,n),r&&e(t,r),t}}();function f(e,t){if(!e)throw new ReferenceError("this hasn't been initialised - super() hasn't been called");return!t||"object"!=typeof t&&"function"!=typeof t?e:t}var h=function(e){function t(){var e,n,r;!function(e,t){if(!(e instanceof t))throw new TypeError("Cannot call a class as a function")}(this,t);for(var a=arguments.length,s=Array(a),i=0;i<a;i++)s[i]=arguments[i];return n=r=f(this,(e=t.__proto__||Object.getPrototypeOf(t)).call.apply(e,[this].concat(s))),r.handle_input=function(e){r.props.textChanged(e.target.value)},r.handle_clear=function(){r.props.textChanged("")},f(r,n)}return function(e,t){if("function"!=typeof t&&null!==t)throw new TypeError("Super expression must either be null or a function, not "+typeof t);e.prototype=Object.create(t&&t.prototype,{constructor:{value:e,enumerable:!1,writable:!0,configurable:!0}}),t&&(Object.setPrototypeOf?Object.setPrototypeOf(e,t):e.__proto__=t)}(t,s.a.PureComponent),p(t,[{key:"render",value:function(){return s.a.createElement("div",{className:(this.props.className?this.props.className+" ":"")+"DqSearchBox__root"},s.a.createElement("input",{className:"DqSearchBox__input",type:"text",placeholder:this.props.placeholder,value:this.props.text,onChange:this.handle_input}),s.a.createElement("div",{className:"DqSearchBox__clear",onClick:this.handle_clear},s.a.createElement(_.a,{name:"cancel"})))}}]),t}();h.propTypes={text:o.a.string.isRequired,textChanged:o.a.func.isRequired,placeholder:o.a.string,className:o.a.string},h.defaultProps={placeholder:"search..."},h.displayName="DqSearchBox";var m=h,d=n(30),y=(n(1324),n(140)),w=n(33),g=n(5),b=n(62),v=n(111),k=n.n(v),R=function(){function e(e,t){for(var n=0;n<t.length;n++){var r=t[n];r.enumerable=r.enumerable||!1,r.configurable=!0,"value"in r&&(r.writable=!0),Object.defineProperty(e,r.key,r)}}return function(t,n,r){return n&&e(t.prototype,n),r&&e(t,r),t}}();function x(e,t){if(!e)throw new ReferenceError("this hasn't been initialised - super() hasn't been called");return!t||"object"!=typeof t&&"function"!=typeof t?e:t}var q=function(e){function t(){var e,n,r;!function(e,t){if(!(e instanceof t))throw new TypeError("Cannot call a class as a function")}(this,t);for(var a=arguments.length,s=Array(a),i=0;i<a;i++)s[i]=arguments[i];return n=r=x(this,(e=t.__proto__||Object.getPrototypeOf(t)).call.apply(e,[this].concat(s))),r.on_open=function(){return r.props.get_takeaways({sequence:r.props.sequence})},x(r,n)}return function(e,t){if("function"!=typeof t&&null!==t)throw new TypeError("Super expression must either be null or a function, not "+typeof t);e.prototype=Object.create(t&&t.prototype,{constructor:{value:e,enumerable:!1,writable:!0,configurable:!0}}),t&&(Object.setPrototypeOf?Object.setPrototypeOf(e,t):e.__proto__=t)}(t,s.a.PureComponent),R(t,[{key:"render_new",value:function(){return this.props.is_new?s.a.createElement(b.a,{className:"ReferenceItem__new"},"New"):null}},{key:"render_completed",value:function(){var e=this.props.time_completed;return e?s.a.createElement("div",{className:"ReferenceItem__time"},"Completed: ",s.a.createElement(k.a,{datetime:e})):null}},{key:"render_icon",value:function(){return s.a.createElement(_.a,{name:this.props.has_takeaways?"file":"ellipsis-h",className:"ReferenceItem__icon"})}},{key:"render_children",value:function(){return s.a.createElement("div",{className:"ReferenceItem__childBox"},s.a.createElement(y.a,{progress:this.props.progress,is_behind_paywall:this.props.is_behind_paywall}),s.a.createElement("div",{className:"ReferenceItem__text"},s.a.createElement("div",{className:"ReferenceItem__title"},s.a.createElement("div",null,this.props.title," ",this.render_new()),this.render_completed()),s.a.createElement("div",{className:"ReferenceItem__description"},this.props.description)),this.render_icon())}},{key:"render",value:function(){var e=Object(w.a)(this.props,this.props);return this.props.has_takeaways?s.a.createElement("div",{className:"ReferenceItem__root",onClick:this.on_open},this.render_children()):s.a.createElement(g.a,{className:"ReferenceItem__root",to:e,href:e},this.render_children())}}]),t}();q.propTypes={title:o.a.string.isRequired,sequence:o.a.string.isRequired,slug:o.a.string,step_index:o.a.number,step_title:o.a.string,description:o.a.string,is_new:o.a.bool,progress:o.a.number.isRequired,is_behind_paywall:o.a.bool,className:o.a.string,matched:o.a.arrayOf(o.a.string).isRequired,time_completed:o.a.string,has_takeaways:o.a.bool,get_takeaways:o.a.func.isRequired},q.defaultProps={matched:[]},q.displayName="ReferenceItem";var O=q,E=n(1173),j=n(8),N=n(12),M=n.n(N),I=n(10),P=n(2),S=n.n(P),C=n(23),B=n(22),T=Object.assign||function(e){for(var t=1;t<arguments.length;t++){var n=arguments[t];for(var r in n)Object.prototype.hasOwnProperty.call(n,r)&&(e[r]=n[r])}return e},D={search_text:"",hits:[],showing_search:!1,searching:!1,takeaways_text:"",current_takeaways_sequence:""},A=Object(I.make_simple_selectors)(D,"mission_reference_info"),J=Object(l.createSelector)(function(e){return C.b.all_missions_by_id(e)},function(e){return S.a.chain(e).filter("time_completed").sortBy("time_completed").reverse().value()}),L=Object(l.createSelector)(J,function(e){return B.d.mission_info(e)},function(e,t){return S.a.filter(e,function(e){return e.sequence!==t.sequence})}),F=Object(l.createSelector)(function(e){return C.b.all_missions_by_id(e)},A.search_text,A.hits,L,function(e,t,n,r){return""===t.trim()?r:S.a.chain(n).map(function(t){var n=t.step_index,r=t.step_title,a=t.mission_sequence,s=t.matched;return T({step_index:n,step_title:r,matched:s},e[a])}).filter(function(e){return null!=e.sequence}).value()}),G=Object(l.createSelector)(function(e){return C.b.all_missions_by_id(e)},function(e){return 0===S.a.keys(e).length}),U=Object(l.createSelector)(A.current_takeaways_sequence,function(e){return Boolean(e)}),Y=Object(l.createSelector)(A.current_takeaways_sequence,A.takeaways_text,F,function(e,t,n){var r=e?S.a.defaultTo(S.a.find(n,{sequence:e}),{}):{};return T({title:"",sequence:"",slug:""},r,{text:t})}),z=T({},A,{missions:F,loading_reference:G,show_takeaways:U,current_takeaways:Y}),H={learn:"objectives",body:"learn_text"},K=function(e){return{mission_sequence:e.mission_sequence,step_index:e.step_index,step_title:e.step_title,matched:function(e){return e.map(function(e){return null!=H[e]?H[e]:e})}(Object.keys(e._highlightResult))}},Q={start_search:function(e,t){var n=t.payload;return e.merge({showing_search:!1,searching:!0,hits:[],search_text:n})},clear_search:function(e,t){var n=t.payload;return e.merge({showing_search:!1,searching:!1,hits:[],search_text:n})},set_results:function(e,t){var n=t.payload;return e.merge({showing_search:!0,searching:!1,hits:n.map(K)})},set_takeaways_sequence:function(e,t){var n=t.payload;return e.merge({takeaways_text:"",current_takeaways_sequence:S.a.defaultTo(n,"")})},set_takeaways:function(e,t){var n=t.payload;return e.merge({takeaways_text:n})}},V=Object(I.make_reducer_n_actions)({public_handlers:{close_takeaways:function(e){return e.merge({takeaways_text:"",current_takeaways_sequence:""})}},private_handlers:Q,action_types_prefix:"mission_reference_info/",initial_state:D,Immutable:M.a}),W=V.reducer,X=V.private_actions,Z=V.actions,$=(V.ACTION_TYPES,W),ee=n(9),te=function(e){var t=e.sequence;return function(e,n){e(X.set_takeaways_sequence(t));var r="{\n    mission(sequence: "+t+") {\n      takeaways\n    }\n  }";return Object(ee.c)(r).then(function(t){e(X.set_takeaways(t.data.mission.takeaways))})}},ne=function(e){return function(t,n){""!==e.trim()?(t(X.start_search(e)),re(e.trim(),t,n)):t(X.clear_search(e))}};ne.algoliasearch=n(1322),ne.mission_index=null;var re=S.a.debounce(function(e,t,n){!function(){if(null==ne.mission_index){var e=ne.algoliasearch("47E4MB1UJI","f5c1f53a0a5004bca876ee9f4e3d5d57");ne.mission_index=e.initIndex("missions")}}(),ne.mission_index.search({query:e}).then(function(e){t(X.set_results(e.hits))}).catch(function(e){console.log(e),t(X.set_results([]))})},200),ae=n(16),se=Object.assign({},Z,r);Object(ae.a)({mission_reference_info:$});n.d(t,"selectors",function(){return le}),n.d(t,"actions",function(){return ue}),n.d(t,"MissionReference",function(){return pe});var ie=Object.assign||function(e){for(var t=1;t<arguments.length;t++){var n=arguments[t];for(var r in n)Object.prototype.hasOwnProperty.call(n,r)&&(e[r]=n[r])}return e},oe=function(){function e(e,t){for(var n=0;n<t.length;n++){var r=t[n];r.enumerable=r.enumerable||!1,r.configurable=!0,"value"in r&&(r.writable=!0),Object.defineProperty(e,r.key,r)}}return function(t,n,r){return n&&e(t.prototype,n),r&&e(t,r),t}}();function ce(e,t){if(!e)throw new ReferenceError("this hasn't been initialised - super() hasn't been called");return!t||"object"!=typeof t&&"function"!=typeof t?e:t}var le=z,ue=se,_e=Object(l.createStructuredSelector)(le),pe=function(e){function t(){var e,n,r;!function(e,t){if(!(e instanceof t))throw new TypeError("Cannot call a class as a function")}(this,t);for(var a=arguments.length,i=Array(a),o=0;o<a;o++)i[o]=arguments[o];return n=r=ce(this,(e=t.__proto__||Object.getPrototypeOf(t)).call.apply(e,[this].concat(i))),r.render_item=function(e){return s.a.createElement(O,ie({key:e.sequence,get_takeaways:r.props.get_takeaways},e))},ce(r,n)}return function(e,t){if("function"!=typeof t&&null!==t)throw new TypeError("Super expression must either be null or a function, not "+typeof t);e.prototype=Object.create(t&&t.prototype,{constructor:{value:e,enumerable:!1,writable:!0,configurable:!0}}),t&&(Object.setPrototypeOf?Object.setPrototypeOf(e,t):e.__proto__=t)}(t,s.a.PureComponent),oe(t,[{key:"render_message",value:function(){return this.props.showing_search?"Found "+this.props.missions.length+" missions":this.props.searching?s.a.createElement(d.a,{className:"MissionReference__searching",message:"Searching missions"}):0===this.props.missions.length?"":"Recently completed missions"}},{key:"render_takeaways_nav",value:function(){var e=this.props.current_takeaways,t=Object(w.a)(e,e);return s.a.createElement("div",{className:"MissionReference__takeaways_header"},s.a.createElement(j.a,{short:!0,hollow:!0,borderless:!0,color:"gray",icon:"left",text:"Back",onClick:this.props.close_takeaways}),s.a.createElement(j.a,{short:!0,link_to:t,text:"Go To Mission"}),s.a.createElement("div",{style:{width:"95px"}}))}},{key:"render_takeaway",value:function(){var e=this.props.current_takeaways;return""===e.text?s.a.createElement("div",{className:"MissionReference__content"},this.render_takeaways_nav(),s.a.createElement(d.a,{smaller:!0,message:"Loading takeaways"})):s.a.createElement("div",{className:"MissionReference__takeaways"},this.render_takeaways_nav(),s.a.createElement(E.a,ie({className:"MissionReference__takeaway_text"},e)),this.render_takeaways_nav())}},{key:"render_body",value:function(){return this.props.loading_reference?s.a.createElement("div",{className:"MissionReference__content"},s.a.createElement(d.a,{smaller:!0,message:"Loading missions"})):this.props.show_takeaways?this.render_takeaway():s.a.createElement("div",{className:"MissionReference__content"},s.a.createElement("div",{className:"MissionReference__search"},s.a.createElement(m,{text:this.props.search_text,textChanged:this.props.search_update}),s.a.createElement("div",{className:"MissionReference__search_message"},this.render_message())),s.a.createElement("div",{className:"MissionReference__missions"},this.props.missions.map(this.render_item)))}},{key:"render",value:function(){return s.a.createElement("div",{className:"MissionReference__root"},s.a.createElement(u.a,{title:"Mission Reference",theme:this.props.theme}),this.render_body())}}]),t}();pe.propTypes={loading_reference:o.a.bool.isRequired,search_text:o.a.string.isRequired,search_update:o.a.func.isRequired,showing_search:o.a.bool.isRequired,searching:o.a.bool.isRequired,missions:o.a.arrayOf(o.a.shape({sequence:o.a.string.isRequired})).isRequired,show_takeaways:o.a.bool.isRequired,current_takeaways:o.a.shape({title:o.a.string.isRequired,sequence:o.a.string.isRequired,slug:o.a.string.isRequired,text:o.a.string.isRequired}).isRequired,get_takeaways:o.a.func.isRequired,close_takeaways:o.a.func.isRequired,theme:o.a.string},pe.defaultProps={},pe.displayName="MissionReference";t.default=Object(c.b)(_e,ue)(pe)}}]);