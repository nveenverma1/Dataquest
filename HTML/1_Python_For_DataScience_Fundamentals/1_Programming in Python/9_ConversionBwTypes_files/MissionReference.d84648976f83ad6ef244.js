(window.webpackJsonp=window.webpackJsonp||[]).push([[33],{1477:function(e,t,n){"use strict";n.r(t);var r={};n.r(r),n.d(r,"get_takeaways",function(){return te}),n.d(r,"search_update",function(){return ne});var a=n(0),s=n.n(a),i=n(1),o=n.n(i),c=n(15),l=n(5),u=(n(795),n(665)),_=(n(793),n(37)),p=function(){function e(e,t){for(var n=0;n<t.length;n++){var r=t[n];r.enumerable=r.enumerable||!1,r.configurable=!0,"value"in r&&(r.writable=!0),Object.defineProperty(e,r.key,r)}}return function(t,n,r){return n&&e(t.prototype,n),r&&e(t,r),t}}();function f(e,t){if(!e)throw new ReferenceError("this hasn't been initialised - super() hasn't been called");return!t||"object"!=typeof t&&"function"!=typeof t?e:t}var h=function(e){function t(){var e,n,r;!function(e,t){if(!(e instanceof t))throw new TypeError("Cannot call a class as a function")}(this,t);for(var a=arguments.length,s=Array(a),i=0;i<a;i++)s[i]=arguments[i];return n=r=f(this,(e=t.__proto__||Object.getPrototypeOf(t)).call.apply(e,[this].concat(s))),r.handle_input=function(e){r.props.textChanged(e.target.value)},r.handle_clear=function(){r.props.textChanged("")},f(r,n)}return function(e,t){if("function"!=typeof t&&null!==t)throw new TypeError("Super expression must either be null or a function, not "+typeof t);e.prototype=Object.create(t&&t.prototype,{constructor:{value:e,enumerable:!1,writable:!0,configurable:!0}}),t&&(Object.setPrototypeOf?Object.setPrototypeOf(e,t):e.__proto__=t)}(t,s.a.PureComponent),p(t,[{key:"render",value:function(){return s.a.createElement("div",{className:(this.props.className?this.props.className+" ":"")+"DqSearchBox__root"},s.a.createElement("input",{className:"DqSearchBox__input",type:"text",placeholder:this.props.placeholder,value:this.props.text,onChange:this.handle_input}),s.a.createElement("div",{className:"DqSearchBox__clear",onClick:this.handle_clear},s.a.createElement(_.a,{name:"cancel"})))}}]),t}();h.propTypes={text:o.a.string.isRequired,textChanged:o.a.func.isRequired,placeholder:o.a.string,className:o.a.string},h.defaultProps={placeholder:"search..."},h.displayName="DqSearchBox";var m=h,d=n(74),y=(n(791),n(431)),b=n(290),g=n(13),w=n(345),v=n(356),j=n.n(v),k=function(){function e(e,t){for(var n=0;n<t.length;n++){var r=t[n];r.enumerable=r.enumerable||!1,r.configurable=!0,"value"in r&&(r.writable=!0),Object.defineProperty(e,r.key,r)}}return function(t,n,r){return n&&e(t.prototype,n),r&&e(t,r),t}}();function R(e,t){if(!e)throw new ReferenceError("this hasn't been initialised - super() hasn't been called");return!t||"object"!=typeof t&&"function"!=typeof t?e:t}var O=function(e){function t(){var e,n,r;!function(e,t){if(!(e instanceof t))throw new TypeError("Cannot call a class as a function")}(this,t);for(var a=arguments.length,s=Array(a),i=0;i<a;i++)s[i]=arguments[i];return n=r=R(this,(e=t.__proto__||Object.getPrototypeOf(t)).call.apply(e,[this].concat(s))),r.on_open=function(){return r.props.get_takeaways({sequence:r.props.sequence})},R(r,n)}return function(e,t){if("function"!=typeof t&&null!==t)throw new TypeError("Super expression must either be null or a function, not "+typeof t);e.prototype=Object.create(t&&t.prototype,{constructor:{value:e,enumerable:!1,writable:!0,configurable:!0}}),t&&(Object.setPrototypeOf?Object.setPrototypeOf(e,t):e.__proto__=t)}(t,s.a.PureComponent),k(t,[{key:"render_new",value:function(){return this.props.is_new?s.a.createElement(w.a,{className:"ReferenceItem__new"},"New"):null}},{key:"render_completed",value:function(){var e=this.props.time_completed;return e?s.a.createElement("div",{className:"ReferenceItem__time"},"Completed: ",s.a.createElement(j.a,{datetime:e})):null}},{key:"render_icon",value:function(){return s.a.createElement(_.a,{name:this.props.has_takeaways?"file":"ellipsis-h",className:"ReferenceItem__icon"})}},{key:"render_children",value:function(){return s.a.createElement("div",{className:"ReferenceItem__childBox"},s.a.createElement(y.a,{progress:this.props.progress,is_behind_paywall:this.props.is_behind_paywall}),s.a.createElement("div",{className:"ReferenceItem__text"},s.a.createElement("div",{className:"ReferenceItem__title"},s.a.createElement("div",null,this.props.title," ",this.render_new()),this.render_completed()),s.a.createElement("div",{className:"ReferenceItem__description"},this.props.description)),this.render_icon())}},{key:"render",value:function(){var e=Object(b.a)(this.props,this.props);return this.props.has_takeaways?s.a.createElement("div",{className:"ReferenceItem__root",onClick:this.on_open},this.render_children()):s.a.createElement(g.a,{className:"ReferenceItem__root",to:e,href:e},this.render_children())}}]),t}();O.propTypes={title:o.a.string.isRequired,sequence:o.a.string.isRequired,slug:o.a.string,step_index:o.a.number,step_title:o.a.string,description:o.a.string,is_new:o.a.bool,progress:o.a.number.isRequired,is_behind_paywall:o.a.bool,className:o.a.string,matched:o.a.arrayOf(o.a.string).isRequired,time_completed:o.a.string,has_takeaways:o.a.bool,get_takeaways:o.a.func.isRequired},O.defaultProps={matched:[]},O.displayName="ReferenceItem";var x=O,E=n(592),q=n(19),N=n(8),P=n.n(N),C=n(6),I=n(2),M=n.n(I),T=n(38),S=n(25),B=Object.assign||function(e){for(var t=1;t<arguments.length;t++){var n=arguments[t];for(var r in n)Object.prototype.hasOwnProperty.call(n,r)&&(e[r]=n[r])}return e},D={search_text:"",hits:[],showing_search:!1,searching:!1,takeaways_text:"",current_takeaways_sequence:""},z=Object(C.make_simple_selectors)(D,"mission_reference_info"),A=Object(l.createSelector)(function(e){return T.b.all_missions_by_id(e)},function(e){return M.a.chain(e).filter("time_completed").sortBy("time_completed").reverse().value()}),G=Object(l.createSelector)(A,function(e){return S.d.mission_info(e)},function(e,t){return M.a.filter(e,function(e){return e.sequence!==t.sequence})}),J=Object(l.createSelector)(function(e){return T.b.all_missions_by_id(e)},z.search_text,z.hits,G,function(e,t,n,r){return""===t.trim()?r:M.a.chain(n).map(function(t){var n=t.step_index,r=t.step_title,a=t.mission_sequence,s=t.matched;return B({step_index:n,step_title:r,matched:s},e[a])}).filter(function(e){return null!=e.sequence}).value()}),L=Object(l.createSelector)(function(e){return T.b.all_missions_by_id(e)},function(e){return 0===M.a.keys(e).length}),U=Object(l.createSelector)(z.current_takeaways_sequence,function(e){return Boolean(e)}),F=Object(l.createSelector)(z.current_takeaways_sequence,z.takeaways_text,J,function(e,t,n){var r=e?M.a.defaultTo(M.a.find(n,{sequence:e}),{}):{};return B({title:"",sequence:"",slug:""},r,{text:t})}),H=B({},z,{missions:J,loading_reference:L,show_takeaways:U,current_takeaways:F}),W={learn:"objectives",body:"learn_text"},Y=function(e){return{mission_sequence:e.mission_sequence,step_index:e.step_index,step_title:e.step_title,matched:function(e){return e.map(function(e){return null!=W[e]?W[e]:e})}(Object.keys(e._highlightResult))}},K={start_search:function(e,t){var n=t.payload;return e.merge({showing_search:!1,searching:!0,hits:[],search_text:n})},clear_search:function(e,t){var n=t.payload;return e.merge({showing_search:!1,searching:!1,hits:[],search_text:n})},set_results:function(e,t){var n=t.payload;return e.merge({showing_search:!0,searching:!1,hits:n.map(Y)})},set_takeaways_sequence:function(e,t){var n=t.payload;return e.merge({takeaways_text:"",current_takeaways_sequence:M.a.defaultTo(n,"")})},set_takeaways:function(e,t){var n=t.payload;return e.merge({takeaways_text:n})}},Q=Object(C.make_reducer_n_actions)({public_handlers:{close_takeaways:function(e){return e.merge({takeaways_text:"",current_takeaways_sequence:""})}},private_handlers:K,action_types_prefix:"mission_reference_info/",initial_state:D,Immutable:P.a}),V=Q.reducer,X=Q.private_actions,Z=Q.actions,$=(Q.ACTION_TYPES,V),ee=n(4),te=function(e){var t=e.sequence;return function(e,n){e(X.set_takeaways_sequence(t));var r="{\n    mission(sequence: "+t+") {\n      takeaways\n    }\n  }";return Object(ee.c)(r).then(function(t){e(X.set_takeaways(t.data.mission.takeaways))})}},ne=function(e){return function(t,n){""!==e.trim()?(t(X.start_search(e)),re(e.trim(),t,n)):t(X.clear_search(e))}};ne.algoliasearch=n(789),ne.mission_index=null;var re=M.a.debounce(function(e,t,n){!function(){if(null==ne.mission_index){var e=ne.algoliasearch("47E4MB1UJI","f5c1f53a0a5004bca876ee9f4e3d5d57");ne.mission_index=e.initIndex("missions")}}(),ne.mission_index.search({query:e}).then(function(e){t(X.set_results(e.hits))}).catch(function(e){console.log(e),t(X.set_results([]))})},200),ae=n(10),se=Object.assign({},Z,r);Object(ae.a)({mission_reference_info:$});n.d(t,"selectors",function(){return le}),n.d(t,"actions",function(){return ue}),n.d(t,"MissionReference",function(){return pe});var ie=Object.assign||function(e){for(var t=1;t<arguments.length;t++){var n=arguments[t];for(var r in n)Object.prototype.hasOwnProperty.call(n,r)&&(e[r]=n[r])}return e},oe=function(){function e(e,t){for(var n=0;n<t.length;n++){var r=t[n];r.enumerable=r.enumerable||!1,r.configurable=!0,"value"in r&&(r.writable=!0),Object.defineProperty(e,r.key,r)}}return function(t,n,r){return n&&e(t.prototype,n),r&&e(t,r),t}}();function ce(e,t){if(!e)throw new ReferenceError("this hasn't been initialised - super() hasn't been called");return!t||"object"!=typeof t&&"function"!=typeof t?e:t}var le=H,ue=se,_e=Object(l.createStructuredSelector)(le),pe=function(e){function t(){var e,n,r;!function(e,t){if(!(e instanceof t))throw new TypeError("Cannot call a class as a function")}(this,t);for(var a=arguments.length,i=Array(a),o=0;o<a;o++)i[o]=arguments[o];return n=r=ce(this,(e=t.__proto__||Object.getPrototypeOf(t)).call.apply(e,[this].concat(i))),r.render_item=function(e){return s.a.createElement(x,ie({key:e.sequence,get_takeaways:r.props.get_takeaways},e))},ce(r,n)}return function(e,t){if("function"!=typeof t&&null!==t)throw new TypeError("Super expression must either be null or a function, not "+typeof t);e.prototype=Object.create(t&&t.prototype,{constructor:{value:e,enumerable:!1,writable:!0,configurable:!0}}),t&&(Object.setPrototypeOf?Object.setPrototypeOf(e,t):e.__proto__=t)}(t,s.a.PureComponent),oe(t,[{key:"render_message",value:function(){return this.props.showing_search?"Found "+this.props.missions.length+" missions":this.props.searching?s.a.createElement(d.a,{className:"MissionReference__searching",message:"Searching missions"}):0===this.props.missions.length?"":"Recently completed missions"}},{key:"render_takeaways_nav",value:function(){var e=this.props.current_takeaways,t=Object(b.a)(e,e);return s.a.createElement("div",{className:"MissionReference__takeaways_header"},s.a.createElement(q.a,{short:!0,hollow:!0,borderless:!0,color:"gray",icon:"left",text:"Back",onClick:this.props.close_takeaways}),s.a.createElement(q.a,{short:!0,link_to:t,text:"Go To Mission"}),s.a.createElement("div",{style:{width:"95px"}}))}},{key:"render_takeaway",value:function(){var e=this.props.current_takeaways;return""===e.text?s.a.createElement("div",{className:"MissionReference__content"},this.render_takeaways_nav(),s.a.createElement(d.a,{smaller:!0,message:"Loading takeaways"})):s.a.createElement("div",{className:"MissionReference__takeaways"},this.render_takeaways_nav(),s.a.createElement(E.a,ie({className:"MissionReference__takeaway_text"},e)),this.render_takeaways_nav())}},{key:"render_body",value:function(){return this.props.loading_reference?s.a.createElement("div",{className:"MissionReference__content"},s.a.createElement(d.a,{smaller:!0,message:"Loading missions"})):this.props.show_takeaways?this.render_takeaway():s.a.createElement("div",{className:"MissionReference__content"},s.a.createElement("div",{className:"MissionReference__search"},s.a.createElement(m,{text:this.props.search_text,textChanged:this.props.search_update}),s.a.createElement("div",{className:"MissionReference__search_message"},this.render_message())),s.a.createElement("div",{className:"MissionReference__missions"},this.props.missions.map(this.render_item)))}},{key:"render",value:function(){return s.a.createElement("div",{className:"MissionReference__root"},s.a.createElement(u.a,{title:"Mission Reference",theme:this.props.theme}),this.render_body())}}]),t}();pe.propTypes={loading_reference:o.a.bool.isRequired,search_text:o.a.string.isRequired,search_update:o.a.func.isRequired,showing_search:o.a.bool.isRequired,searching:o.a.bool.isRequired,missions:o.a.arrayOf(o.a.shape({sequence:o.a.string.isRequired})).isRequired,show_takeaways:o.a.bool.isRequired,current_takeaways:o.a.shape({title:o.a.string.isRequired,sequence:o.a.string.isRequired,slug:o.a.string.isRequired,text:o.a.string.isRequired}).isRequired,get_takeaways:o.a.func.isRequired,close_takeaways:o.a.func.isRequired,theme:o.a.string},pe.defaultProps={},pe.displayName="MissionReference";t.default=Object(c.b)(_e,ue)(pe)},345:function(e,t,n){"use strict";var r=n(0),a=n.n(r),s=n(1),i=n.n(s),o=(n(404),function(){function e(e,t){for(var n=0;n<t.length;n++){var r=t[n];r.enumerable=r.enumerable||!1,r.configurable=!0,"value"in r&&(r.writable=!0),Object.defineProperty(e,r.key,r)}}return function(t,n,r){return n&&e(t.prototype,n),r&&e(t,r),t}}());var c=function(e){function t(){return function(e,t){if(!(e instanceof t))throw new TypeError("Cannot call a class as a function")}(this,t),function(e,t){if(!e)throw new ReferenceError("this hasn't been initialised - super() hasn't been called");return!t||"object"!=typeof t&&"function"!=typeof t?e:t}(this,(t.__proto__||Object.getPrototypeOf(t)).apply(this,arguments))}return function(e,t){if("function"!=typeof t&&null!==t)throw new TypeError("Super expression must either be null or a function, not "+typeof t);e.prototype=Object.create(t&&t.prototype,{constructor:{value:e,enumerable:!1,writable:!0,configurable:!0}}),t&&(Object.setPrototypeOf?Object.setPrototypeOf(e,t):e.__proto__=t)}(t,a.a.PureComponent),o(t,[{key:"render",value:function(){return null==this.props.children?null:a.a.createElement("div",{title:this.props.toolTip,className:(this.props.className?this.props.className+" ":"")+"DqBadge__root"},this.props.children)}}]),t}();c.propTypes={children:i.a.node,toolTip:i.a.string,className:i.a.string},c.defaultProps={},c.displayName="DqBadge",t.a=c},402:function(e,t,n){var r={"./ar":341,"./ar.js":341,"./be":340,"./be.js":340,"./bg":339,"./bg.js":339,"./ca":338,"./ca.js":338,"./da":337,"./da.js":337,"./de":336,"./de.js":336,"./el":335,"./el.js":335,"./en":334,"./en.js":334,"./en_short":333,"./en_short.js":333,"./es":332,"./es.js":332,"./eu":331,"./eu.js":331,"./fa":330,"./fa.js":330,"./fi":329,"./fi.js":329,"./fr":328,"./fr.js":328,"./he":327,"./he.js":327,"./hu":326,"./hu.js":326,"./in_BG":325,"./in_BG.js":325,"./in_HI":324,"./in_HI.js":324,"./in_ID":323,"./in_ID.js":323,"./it":322,"./it.js":322,"./ja":321,"./ja.js":321,"./ko":320,"./ko.js":320,"./locales":319,"./locales.js":319,"./ml":318,"./ml.js":318,"./my":317,"./my.js":317,"./nb_NO":316,"./nb_NO.js":316,"./nl":315,"./nl.js":315,"./nn_NO":314,"./nn_NO.js":314,"./pl":313,"./pl.js":313,"./pt_BR":312,"./pt_BR.js":312,"./ro":311,"./ro.js":311,"./ru":310,"./ru.js":310,"./sv":309,"./sv.js":309,"./ta":308,"./ta.js":308,"./th":307,"./th.js":307,"./tr":306,"./tr.js":306,"./uk":305,"./uk.js":305,"./vi":304,"./vi.js":304,"./zh_CN":303,"./zh_CN.js":303,"./zh_TW":302,"./zh_TW.js":302};function a(e){var t=s(e);return n(t)}function s(e){var t=r[e];if(!(t+1)){var n=new Error("Cannot find module '"+e+"'");throw n.code="MODULE_NOT_FOUND",n}return t}a.keys=function(){return Object.keys(r)},a.resolve=s,e.exports=a,a.id=402},404:function(e,t,n){e.exports={root:"DqBadge__root"}},431:function(e,t,n){"use strict";var r=n(0),a=n.n(r),s=n(1),i=n.n(s),o=(n(538),n(298)),c=n(37),l=function(){function e(e,t){for(var n=0;n<t.length;n++){var r=t[n];r.enumerable=r.enumerable||!1,r.configurable=!0,"value"in r&&(r.writable=!0),Object.defineProperty(e,r.key,r)}}return function(t,n,r){return n&&e(t.prototype,n),r&&e(t,r),t}}();var u=function(e){function t(){return function(e,t){if(!(e instanceof t))throw new TypeError("Cannot call a class as a function")}(this,t),function(e,t){if(!e)throw new ReferenceError("this hasn't been initialised - super() hasn't been called");return!t||"object"!=typeof t&&"function"!=typeof t?e:t}(this,(t.__proto__||Object.getPrototypeOf(t)).apply(this,arguments))}return function(e,t){if("function"!=typeof t&&null!==t)throw new TypeError("Super expression must either be null or a function, not "+typeof t);e.prototype=Object.create(t&&t.prototype,{constructor:{value:e,enumerable:!1,writable:!0,configurable:!0}}),t&&(Object.setPrototypeOf?Object.setPrototypeOf(e,t):e.__proto__=t)}(t,a.a.PureComponent),l(t,[{key:"render",value:function(){var e=this.props,t=e.progress,n=e.is_behind_paywall,r=e.className;return n?a.a.createElement("div",{className:r},a.a.createElement(c.a,{className:"ProgressCircle__locked",name:"lock"})):t>=1?a.a.createElement("div",{className:r},a.a.createElement(c.a,{className:"ProgressCircle__finished",name:"pass"})):a.a.createElement("div",{className:(r?r+" ":"")+"ProgressCircle__in_progress"},a.a.createElement("div",null,Object(o.a)(t)))}}]),t}();u.propTypes={progress:i.a.number.isRequired,is_behind_paywall:i.a.bool,className:i.a.string},u.defaultProps={},u.displayName="ProgressCircle",t.a=u},538:function(e,t,n){e.exports={finished:"ProgressCircle__finished",in_progress:"ProgressCircle__in_progress",locked:"ProgressCircle__locked"}},791:function(e,t,n){e.exports={title:"ReferenceItem__title",description:"ReferenceItem__description",matched:"ReferenceItem__matched",time:"ReferenceItem__time",root:"ReferenceItem__root",childBox:"ReferenceItem__childBox",text:"ReferenceItem__text",matched_list:"ReferenceItem__matched_list",new:"ReferenceItem__new",icon:"ReferenceItem__icon"}},793:function(e,t,n){e.exports={input:"DqSearchBox__input",root:"DqSearchBox__root",clear:"DqSearchBox__clear"}},795:function(e,t,n){e.exports={search_message:"MissionReference__search_message",searching:"MissionReference__searching",root:"MissionReference__root",content:"MissionReference__content",takeaways:"MissionReference__takeaways",takeaway_text:"MissionReference__takeaway_text",takeaways_header:"MissionReference__takeaways_header",search:"MissionReference__search",missions:"MissionReference__missions"}}}]);
//# sourceMappingURL=MissionReference.d84648976f83ad6ef244.js.map