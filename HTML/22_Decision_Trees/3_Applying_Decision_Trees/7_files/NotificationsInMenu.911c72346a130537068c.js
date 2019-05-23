(window.webpackJsonp=window.webpackJsonp||[]).push([[32],{1333:function(e,t,n){e.exports={header:"NotificationItem__header",read:"NotificationItem__read",message:"NotificationItem__message"}},1335:function(e,t,n){e.exports={root:"NotificationPanel__root",notifications:"NotificationPanel__notifications",options:"NotificationPanel__options"}},1337:function(e,t,n){e.exports={root:"NotificationLink__root",badge:"NotificationLink__badge"}},1339:function(e,t,n){},1585:function(e,t,n){"use strict";n.r(t);var r={};n.r(r),n.d(r,"mark_as_read",function(){return U}),n.d(r,"mark_all",function(){return V}),n.d(r,"connect_notifications",function(){return Z});var o=n(0),i=n.n(o),a=n(1),c=n.n(a),s=n(6),u=n(3),f=n(2),l=n.n(f),p=(n(1339),n(1172)),d=(n(1337),n(20)),_=n(62),b=function(){function e(e,t){for(var n=0;n<t.length;n++){var r=t[n];r.enumerable=r.enumerable||!1,r.configurable=!0,"value"in r&&(r.writable=!0),Object.defineProperty(e,r.key,r)}}return function(t,n,r){return n&&e(t.prototype,n),r&&e(t,r),t}}();var m=function(e){function t(){return function(e,t){if(!(e instanceof t))throw new TypeError("Cannot call a class as a function")}(this,t),function(e,t){if(!e)throw new ReferenceError("this hasn't been initialised - super() hasn't been called");return!t||"object"!=typeof t&&"function"!=typeof t?e:t}(this,(t.__proto__||Object.getPrototypeOf(t)).apply(this,arguments))}return function(e,t){if("function"!=typeof t&&null!==t)throw new TypeError("Super expression must either be null or a function, not "+typeof t);e.prototype=Object.create(t&&t.prototype,{constructor:{value:e,enumerable:!1,writable:!0,configurable:!0}}),t&&(Object.setPrototypeOf?Object.setPrototypeOf(e,t):e.__proto__=t)}(t,i.a.PureComponent),b(t,[{key:"render",value:function(){return i.a.createElement("div",{className:"NotificationLink__root"},i.a.createElement(d.a,{name:"alerts"}),this.props.unread_count>0&&i.a.createElement(_.a,{className:"NotificationLink__badge",toolTip:"Number of unread notifications"},this.props.unread_count))}}]),t}();m.propTypes={unread_count:c.a.number.isRequired},m.defaultProps={},m.displayName="NotificationLink";var y=m,h=(n(1335),n(1333),n(63)),v=n(27),g=n(111),O=n.n(g),k=function(){function e(e,t){for(var n=0;n<t.length;n++){var r=t[n];r.enumerable=r.enumerable||!1,r.configurable=!0,"value"in r&&(r.writable=!0),Object.defineProperty(e,r.key,r)}}return function(t,n,r){return n&&e(t.prototype,n),r&&e(t,r),t}}();function w(e,t){if(!e)throw new ReferenceError("this hasn't been initialised - super() hasn't been called");return!t||"object"!=typeof t&&"function"!=typeof t?e:t}var j=function(e){function t(){var e,n,r;!function(e,t){if(!(e instanceof t))throw new TypeError("Cannot call a class as a function")}(this,t);for(var o=arguments.length,i=Array(o),a=0;a<o;a++)i[a]=arguments[a];return n=r=w(this,(e=t.__proto__||Object.getPrototypeOf(t)).call.apply(e,[this].concat(i))),r._mark_as_read=function(e){r.props.mark_as_read(r.props.id)},w(r,n)}return function(e,t){if("function"!=typeof t&&null!==t)throw new TypeError("Super expression must either be null or a function, not "+typeof t);e.prototype=Object.create(t&&t.prototype,{constructor:{value:e,enumerable:!1,writable:!0,configurable:!0}}),t&&(Object.setPrototypeOf?Object.setPrototypeOf(e,t):e.__proto__=t)}(t,i.a.PureComponent),k(t,[{key:"render",value:function(){var e=Boolean(this.props.read);return i.a.createElement("div",null,i.a.createElement("div",{className:"NotificationItem__header"},i.a.createElement(O.a,{datetime:this.props.created}),i.a.createElement(v.a,{className:"NotificationItem__read",onDark:!0,plainText:!0,icon:"pass",title:e?"Already read":"Mark as read",onClick:this._mark_as_read,disabled:e,selected:e})),i.a.createElement(h.a,{className:"NotificationItem__message",source:this.props.message}))}}]),t}();j.propTypes={id:c.a.string.isRequired,read:c.a.oneOfType([c.a.bool,c.a.string]).isRequired,created:c.a.string.isRequired,message:c.a.string.isRequired,mark_as_read:c.a.func.isRequired},j.defaultProps={},j.displayName="NotificationItem";var N=j,P=Object.assign||function(e){for(var t=1;t<arguments.length;t++){var n=arguments[t];for(var r in n)Object.prototype.hasOwnProperty.call(n,r)&&(e[r]=n[r])}return e},E=function(){function e(e,t){for(var n=0;n<t.length;n++){var r=t[n];r.enumerable=r.enumerable||!1,r.configurable=!0,"value"in r&&(r.writable=!0),Object.defineProperty(e,r.key,r)}}return function(t,n,r){return n&&e(t.prototype,n),r&&e(t,r),t}}();function R(e,t){if(!e)throw new ReferenceError("this hasn't been initialised - super() hasn't been called");return!t||"object"!=typeof t&&"function"!=typeof t?e:t}var T=function(e){function t(){var e,n,r;!function(e,t){if(!(e instanceof t))throw new TypeError("Cannot call a class as a function")}(this,t);for(var o=arguments.length,a=Array(o),c=0;c<o;c++)a[c]=arguments[c];return n=r=R(this,(e=t.__proto__||Object.getPrototypeOf(t)).call.apply(e,[this].concat(a))),r.render_note=function(e){return i.a.createElement(N,P({key:e.id},e,{mark_as_read:r.props.mark_as_read}))},R(r,n)}return function(e,t){if("function"!=typeof t&&null!==t)throw new TypeError("Super expression must either be null or a function, not "+typeof t);e.prototype=Object.create(t&&t.prototype,{constructor:{value:e,enumerable:!1,writable:!0,configurable:!0}}),t&&(Object.setPrototypeOf?Object.setPrototypeOf(e,t):e.__proto__=t)}(t,i.a.PureComponent),E(t,[{key:"render_notifications",value:function(){return 0===this.props.notifications.length?i.a.createElement("div",null,"No notifications"):this.props.notifications.map(this.render_note)}},{key:"render",value:function(){return i.a.createElement("div",{className:"NotificationPanel__root"},i.a.createElement("div",{className:"NotificationPanel__notifications"},this.render_notifications()),i.a.createElement("div",{className:"NotificationPanel__options"},i.a.createElement(v.a,{onDark:!0,toolbar:!0,text:"Mark all as Read",onClick:this.props.mark_all})))}}]),t}();T.propTypes={notifications:c.a.array.isRequired,mark_as_read:c.a.func.isRequired,mark_all:c.a.func.isRequired},T.defaultProps={},T.displayName="NotificationPanel";var q=T,C=n(12),I=n.n(C),x=n(10),S=Object.assign||function(e){for(var t=1;t<arguments.length;t++){var n=arguments[t];for(var r in n)Object.prototype.hasOwnProperty.call(n,r)&&(e[r]=n[r])}return e};var L={notifications:{}},M=Object(x.make_simple_selectors)(L,"notifications_info"),A=S({},M,{notifications:Object(u.createSelector)(M.notifications,function(e){var t=Date.now()-6048e5;return l.a.chain(e).filter(function(e){var n=e.read;return!1===n||!0===n||Date.parse(n)>t}).sortBy("created").reverse().value()}),unread_count:Object(u.createSelector)(M.notifications,function(e){return l.a.filter(e,{read:!1}).length})}),D={reset:function(){return I()(L)}};function B(e){return{id:l.a.toString(e.id),created:e.created,read:e.seen||!1,message:e.message||l.a.get(e.data,"message")}}var J={add_notifications:function(e,t){var n=t.payload;return e.merge({notifications:n.reduce(function(e,t){return e[(t=B(t)).id]=t,e},{})},{deep:!0})},add_notification_ws:function(e,t){var n=B(t.payload);return e.merge({notifications:function(e,t,n){return t in e?Object.defineProperty(e,t,{value:n,enumerable:!0,configurable:!0,writable:!0}):e[t]=n,e}({},n.id,n)},{deep:!0})},set_read:function(e,t){var n=t.payload;return e.merge({notifications:n.reduce(function(e,t){return e[t]={read:!0},e},{})},{deep:!0})}},W=Object(x.make_reducer_n_actions)({public_handlers:D,private_handlers:J,action_types_prefix:"notifications_info/",initial_state:L,Immutable:I.a}),Y=W.reducer,z=W.private_actions,F=W.actions,G=W.ACTION_TYPES,H=Y,K=n(9),Q=n(34),U=function(e){return function(t,n){return X([e])(t,n)}},V=function(e){return function(e,t){var n=l.a.map(l.a.filter(A.notifications(t()),{read:!1}),"id");return X(n)(e,t)}},X=function(e){return function(t,n){var r={seen:e};return Object(K.b)("/api/v2/notifications/notifications/seen/",{post_obj:r}).then(function(n){t(z.set_read(e))}).catch(console.error)}},Z=function(){return function(e,t){return e(Q.a.connect({"push/notifications":G.add_notification_ws})),Object(K.b)("/api/v2/notifications/notifications/").then(function(t){e(z.add_notifications(t))}).catch(console.error)}},$=n(16),ee=Object.assign({},F,r),te=(Object($.a)({notifications_info:H}),n(4));n.d(t,"selectors",function(){return re}),n.d(t,"actions",function(){return oe}),n.d(t,"NotificationsInMenu",function(){return ae});var ne=function(){function e(e,t){for(var n=0;n<t.length;n++){var r=t[n];r.enumerable=r.enumerable||!1,r.configurable=!0,"value"in r&&(r.writable=!0),Object.defineProperty(e,r.key,r)}}return function(t,n,r){return n&&e(t.prototype,n),r&&e(t,r),t}}();var re=(Object.assign||function(e){for(var t=1;t<arguments.length;t++){var n=arguments[t];for(var r in n)Object.prototype.hasOwnProperty.call(n,r)&&(e[r]=n[r])}return e})({},A,{is_logged_in:te.b.is_logged_in}),oe=ee,ie=Object(u.createStructuredSelector)(re),ae=function(e){function t(){return function(e,t){if(!(e instanceof t))throw new TypeError("Cannot call a class as a function")}(this,t),function(e,t){if(!e)throw new ReferenceError("this hasn't been initialised - super() hasn't been called");return!t||"object"!=typeof t&&"function"!=typeof t?e:t}(this,(t.__proto__||Object.getPrototypeOf(t)).apply(this,arguments))}return function(e,t){if("function"!=typeof t&&null!==t)throw new TypeError("Super expression must either be null or a function, not "+typeof t);e.prototype=Object.create(t&&t.prototype,{constructor:{value:e,enumerable:!1,writable:!0,configurable:!0}}),t&&(Object.setPrototypeOf?Object.setPrototypeOf(e,t):e.__proto__=t)}(t,i.a.PureComponent),ne(t,[{key:"componentWillMount",value:function(){this.check_to_connect(this.props,{})}},{key:"componentWillReceiveProps",value:function(e){this.check_to_connect(e,this.props)}},{key:"check_to_connect",value:function(e,t){e.is_logged_in&&!t.is_logged_in&&e.connect_notifications()}},{key:"render",value:function(){return i.a.createElement(p.a,{dropdown:i.a.createElement(q,l.a.pick(this.props,["notifications","mark_as_read","mark_all"])),selector:i.a.createElement(y,{unread_count:this.props.unread_count})})}}]),t}();ae.propTypes={is_logged_in:c.a.bool.isRequired,notifications:c.a.array.isRequired,unread_count:c.a.number.isRequired,mark_as_read:c.a.func.isRequired,mark_all:c.a.func.isRequired,connect_notifications:c.a.func.isRequired},ae.displayName="NotificationsInMenu";t.default=Object(s.b)(ie,oe)(ae)}}]);