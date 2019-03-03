(window.webpackJsonp=window.webpackJsonp||[]).push([[39],{1463:function(e,n,r){"use strict";r.r(n),r.d(n,"MissionFileViewer",function(){return w});var t=r(14),i=r.n(t),o=r(0),a=r.n(o),s=r(1),l=r.n(s),u=r(598),c=(r(640),r(2)),d=r.n(c),p=(r(845),r(354)),_=function(){function e(e,n){for(var r=0;r<n.length;r++){var t=n[r];t.enumerable=t.enumerable||!1,t.configurable=!0,"value"in t&&(t.writable=!0),Object.defineProperty(e,t.key,t)}}return function(n,r,t){return r&&e(n.prototype,r),t&&e(n,t),n}}(),h={"./MissionFileViewer.scss":{none:"MissionFileViewer__none",dark:"MissionFileViewer__dark",header:"MissionFileViewer__header",light:"MissionFileViewer__light",even:"MissionFileViewer__even",odd:"MissionFileViewer__odd",not_first_column:"MissionFileViewer__not_first_column"}};function f(e,n){if(!e)throw new ReferenceError("this hasn't been initialised - super() hasn't been called");return!n||"object"!=typeof n&&"function"!=typeof n?e:n}var w=function(e){function n(){var e,r,t;!function(e,n){if(!(e instanceof n))throw new TypeError("Cannot call a class as a function")}(this,n);for(var o=arguments.length,s=Array(o),l=0;l<o;l++)s[l]=arguments[l];return r=t=f(this,(e=n.__proto__||Object.getPrototypeOf(n)).call.apply(e,[this].concat(s))),t.rowClassName=function(e){if(e<0)return"header";return e%2==0?"even":"odd"},t.cellRenderer=function(e){var n=e.columnIndex,r=e.key,o=e.rowIndex,s=e.style,l=d.a.get(t.props.preview.data.rows,[o,n],"");return a.a.createElement("div",{key:r,style:s,title:l,className:i()(t.rowClassName(o)+(0===n?"":" not_first_column"),h)},l)},f(t,r)}return function(e,n){if("function"!=typeof n&&null!==n)throw new TypeError("Super expression must either be null or a function, not "+typeof n);e.prototype=Object.create(n&&n.prototype,{constructor:{value:e,enumerable:!1,writable:!0,configurable:!0}}),n&&(Object.setPrototypeOf?Object.setPrototypeOf(e,n):e.__proto__=n)}(n,a.a.PureComponent),_(n,[{key:"get_columnWidth",value:function(e,n){return Math.max(100,Math.round(e/n))}},{key:"render_table",value:function(){var e=this,n=this.props.preview.data,r=n.rows,t=n.column_length;return a.a.createElement("div",{className:i()(this.props.theme,h)},a.a.createElement(u.a,null,function(n){var i=n.height,o=n.width;return a.a.createElement(u.d,{data:e.props.preview.data,cellRenderer:e.cellRenderer,columnCount:t,columnWidth:e.get_columnWidth(o,t),width:o,height:i,rowCount:r.length,rowHeight:20})}))}},{key:"render_text",value:function(){return a.a.createElement(p.a,{value:JSON.stringify(this.props.preview.data),mode:"text",readOnly:!0,onDark:"dark"===this.props.theme})}},{key:"render_none",value:function(){return a.a.createElement("div",{className:"MissionFileViewer__none"},a.a.createElement("h3",null,"This file cannot be previewed as it is a binary file."))}},{key:"render",value:function(){switch(this.props.preview.type){case"text":return this.render_text();case"table":return this.render_table()}return this.render_none()}}]),n}();w.propTypes={container_path:l.a.string.isRequired,name:l.a.string.isRequired,preview:l.a.shape({data:l.a.any.isRequired,type:l.a.string.isRequired}).isRequired,s3_url:l.a.string.isRequired,theme:l.a.string},w.defaultProps={theme:"dark"},w.displayName="MissionFileViewer",n.default=w},845:function(e,n,r){e.exports={none:"MissionFileViewer__none",dark:"MissionFileViewer__dark",light:"MissionFileViewer__light",header:"MissionFileViewer__header",even:"MissionFileViewer__even",odd:"MissionFileViewer__odd",not_first_column:"MissionFileViewer__not_first_column"}}}]);
//# sourceMappingURL=MissionFileViewer.1c18e0f77113bd4f1df8.js.map