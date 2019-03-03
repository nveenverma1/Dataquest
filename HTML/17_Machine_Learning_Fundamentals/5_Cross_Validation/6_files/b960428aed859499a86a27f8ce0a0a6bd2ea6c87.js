window.hellobarSiteSettings=window.hellobarSiteSettings||{"preview_is_active":false,"capabilities":{"autofills":false,"geolocation_injection":false,"external_tracking":false},"site_id":546010,"site_url":"https://www.dataquest.io","pro_secret":"ld3ea0b943d4f148456cccbb58a2fac1b9c4400bc","site_timezone":"-05:00","hellobar_container_css":"#hellobar-container.HB-Modal{top:0;left:0;position:fixed;_position:absolute;_top:expression(eval(document.body.scrollTop));width:100%;height:100%;z-index:10000003}#hellobar-container.HB-Modal.hb-animated{opacity:0;height:110%;margin-top:-5%}#hellobar-container.HB-Modal.hb-animateIn{animation-name:hb-fadeInDown;-o-animation-name:hb-fadeInDown;-ms-animation-name:hb-fadeInDown;-moz-animation-name:hb-fadeInDown;-webkit-animation-name:hb-fadeInDown}#hellobar-container.HB-Modal.hb-animateOut{animation-name:hb-fadeOutUp;-o-animation-name:hb-fadeOutUp;-ms-animation-name:hb-fadeOutUp;-moz-animation-name:hb-fadeOutUp;-webkit-animation-name:hb-fadeOutUp}\n\n","templates":[{"name":"modal_announcement","markup":"\u003cdiv id=\"hellobar-modal-background\"\u003e\u003c/div\u003e\n\n\u003cdiv id=\"hellobar-modal\" class=\"js-hellobar-element {{siteElement.placement}} {{siteElement.imagePlacementClass()}} {{siteElement.brightnessClass()}} {{siteElement.accountCssClass()}} {{siteElement.brandingCssClass()}}\" style=\"background-color: #{{siteElement.primary_color}}; color: #{{siteElement.text_color}}; font-family: {{siteElement.font}};\"\u003e\n  {{siteElement.imageFor('background')}}\n\n  \u003cdiv class=\"hb-header\" style=\"background-color: #{{siteElement.button_color}}\"\u003e\u003c/div\u003e\n\n  {{siteElement.imageFor('left')}}\n\n  \u003cdiv class=\"hb-content-wrapper\"\u003e\n    \u003cdiv class=\"hb-inner-content\"\u003e\n      {{siteElement.imageFor('top')}}\n      \u003cdiv class=\"hb-text-wrapper\"\u003e\n        \u003cdiv class=\"hb-headline-text {{siteElement.questionOrAnswerOrThankYouIsShown() ? '' : 'hb-editable-block hb-editable-block-with-full-formatting'}}\"\n             data-hb-editable-block=\"headline\"\n             data-hb-inline-editor-placeholder=\"Headline\"style=\"{{siteElement.thankYouStyle()}}\"\u003e\n          {{siteElement.headline}}\n        \u003c/div\u003e\n        {{siteElement.imageFor('above-caption')}}\n        \u003cdiv style=\"{{siteElement.showCaption() ? 'display: block;' : 'display: none;'}}\"\u003e\n        \u003cdiv class=\"hb-secondary-text {{siteElement.questionOrAnswerOrThankYouIsShown() ? '' : 'hb-editable-block hb-editable-block-optional hb-editable-block-with-full-formatting'}}\"\n             data-hb-editable-block=\"caption\"\n             data-hb-inline-editor-placeholder=\"Optional Subheadline 1\"\u003e\n          {{siteElement.caption}}\n        \u003c/div\u003e\n        \u003c/div\u003e\n        \u003cdiv style=\"{{siteElement.showContent() ? 'display: block;' : 'display: none;'}}\"\u003e\n        \u003cdiv class=\"hb-secondary-text {{siteElement.questionOrAnswerOrThankYouIsShown() ? '' : 'hb-editable-block hb-editable-block-optional hb-editable-block-with-full-formatting'}}\"\n             data-hb-editable-block=\"content\"\n             data-hb-inline-editor-placeholder=\"Optional Subheadline 2\"\u003e\n          {{siteElement.content}}\n        \u003c/div\u003e\n        \u003c/div\u003e\n        {{siteElement.imageFor('below-caption')}}\n      \u003c/div\u003e\n\u003c!-- nothing to do here --\u003e\n      {{siteElement.imageFor('bottom')}}\n      \u003cdiv style=\"{{siteElement.isAnnouncement() ? 'display: none;' : 'display: block;'}}\"\u003e\n      \u003cdiv class=\"no-thanks-wrapper hb-secondary-text hb-editable-block-with-full-formatting\"\n           data-hb-editable-block=\"no_thanks_text\"\n           data-hb-inline-editor-placeholder=\"No, Thanks\"\n           style=\" {{siteElement.noThanksIsShown() ? 'display: none;' : 'display: block;'}}\"\u003e\n          \u003cdiv onclick=\"{{siteElement.me}}.close()\" \u003e{{siteElement.no_thanks_text}}\u003c/div\u003e\n      \u003c/div\u003e\n      \u003c/div\u003e\n      \u003cdiv class=\"hb-logo-wrapper {{hellobar('base.coloring').colorIsBright(siteElement.primary_color) ? 'hb-logo-inverted' : ''}} {{siteElement.brandingName()}}\" \u003e\n        {{siteElement.renderBranding()}}\n      \u003c/div\u003e\n    \u003c/div\u003e\n  \u003c/div\u003e\n\n  {{siteElement.imageFor('right')}}\n\n  \u003ca class=\"icon-close\" onclick=\"{{siteElement.me}}.close()\"\u003e\u003c/a\u003e\n\u003c/div\u003e\n"},{"name":"modal_thankyou","markup":"\u003cdiv id=\"hellobar-modal-background\"\u003e\u003c/div\u003e\n\n\u003cdiv id=\"hellobar-modal\" class=\"js-hellobar-element {{siteElement.placement}} {{siteElement.imagePlacementClass()}} {{siteElement.brightnessClass()}} {{siteElement.accountCssClass()}} {{siteElement.brandingCssClass()}}\" style=\"background-color: #{{siteElement.primary_color}}; color: #{{siteElement.text_color}}; font-family: {{siteElement.font}};\"\u003e\n  {{siteElement.imageFor('background')}}\n\n  \u003cdiv class=\"hb-header\" style=\"background-color: #{{siteElement.button_color}}\"\u003e\u003c/div\u003e\n\n  {{siteElement.imageFor('left')}}\n\n  \u003cdiv class=\"hb-content-wrapper\"\u003e\n    \u003cdiv class=\"hb-inner-content\"\u003e\n      {{siteElement.imageFor('top')}}\n      \u003cdiv class=\"hb-text-wrapper\"\u003e\n        \u003cdiv class=\"hb-headline-text {{siteElement.questionOrAnswerOrThankYouIsShown() ? '' : 'hb-editable-block hb-editable-block-with-full-formatting'}}\"\n             data-hb-editable-block=\"headline\"\n             data-hb-inline-editor-placeholder=\"Headline\"style=\"{{siteElement.thankYouStyle()}}\"\u003e\n          {{siteElement.headline}}\n        \u003c/div\u003e\n        {{siteElement.imageFor('above-caption')}}\n        \u003cdiv style=\"{{siteElement.showCaption() ? 'display: block;' : 'display: none;'}}\"\u003e\n        \u003cdiv class=\"hb-secondary-text {{siteElement.questionOrAnswerOrThankYouIsShown() ? '' : 'hb-editable-block hb-editable-block-optional hb-editable-block-with-full-formatting'}}\"\n             data-hb-editable-block=\"caption\"\n             data-hb-inline-editor-placeholder=\"Optional Subheadline 1\"\u003e\n          {{siteElement.caption}}\n        \u003c/div\u003e\n        \u003c/div\u003e\n        \u003cdiv style=\"{{siteElement.showContent() ? 'display: block;' : 'display: none;'}}\"\u003e\n        \u003cdiv class=\"hb-secondary-text {{siteElement.questionOrAnswerOrThankYouIsShown() ? '' : 'hb-editable-block hb-editable-block-optional hb-editable-block-with-full-formatting'}}\"\n             data-hb-editable-block=\"content\"\n             data-hb-inline-editor-placeholder=\"Optional Subheadline 2\"\u003e\n          {{siteElement.content}}\n        \u003c/div\u003e\n        \u003c/div\u003e\n        {{siteElement.imageFor('below-caption')}}\n      \u003c/div\u003e\n\u003ca id=\"hb-answer1\" href=\"javascript:void(0);\" onclick=\"{{siteElement.me}}.findById(siteElement.id).close()\" class=\"{{siteElement.ctaClass()}} answer\" style=\"{{siteElement.ctaStyle()}}\"\u003e\n  \u003cdiv class=\"hb-text-holder\"\u003e\n   Close\n  \u003c/div\u003e\n\u003c/a\u003e      {{siteElement.imageFor('bottom')}}\n      \u003cdiv style=\"{{siteElement.isAnnouncement() ? 'display: none;' : 'display: block;'}}\"\u003e\n      \u003cdiv class=\"no-thanks-wrapper hb-secondary-text hb-editable-block-with-full-formatting\"\n           data-hb-editable-block=\"no_thanks_text\"\n           data-hb-inline-editor-placeholder=\"No, Thanks\"\n           style=\" {{siteElement.noThanksIsShown() ? 'display: none;' : 'display: block;'}}\"\u003e\n          \u003cdiv onclick=\"{{siteElement.me}}.close()\" \u003e{{siteElement.no_thanks_text}}\u003c/div\u003e\n      \u003c/div\u003e\n      \u003c/div\u003e\n      \u003cdiv class=\"hb-logo-wrapper {{hellobar('base.coloring').colorIsBright(siteElement.primary_color) ? 'hb-logo-inverted' : ''}} {{siteElement.brandingName()}}\" \u003e\n        {{siteElement.renderBranding()}}\n      \u003c/div\u003e\n    \u003c/div\u003e\n  \u003c/div\u003e\n\n  {{siteElement.imageFor('right')}}\n\n  \u003ca class=\"icon-close\" onclick=\"{{siteElement.me}}.close()\"\u003e\u003c/a\u003e\n\u003c/div\u003e\n"}],"gdpr_enabled":false,"gdpr_consent":"I consent to occasionally receive newsletter, promotional, partnership, product/service, and market research emails.","gdpr_agreement":"I have read and agree to the \u003ca target=\"_blank\" href=\"\"\u003ePrivacy Policy\u003c/a\u003e and \u003ca target=\"_blank\" href=\"\"\u003eTerms and Conditions\u003c/a\u003e.","gdpr_action":"Submit","geolocation_url":"https://pro.ip-api.com/json?key=lhUOBUhHc0DLTCM","tracking_url":"https://hi.hellobar.com","site_write_key":"26e4bbdc-d03f-464b-888f-38bc2c8b9948","external_tracking":[],"hellobar_element_css":"#hellobar-modal{left:50%;padding:48px;position:fixed;max-width:41em;text-align:center;font-size:16px;transform:translateX(-50%);-o-transform:translateX(-50%);-ms-transform:translateX(-50%);-moz-transform:translateX(-50%);-webkit-transform:translateX(-50%)}#hellobar-modal-background{top:0px;left:0px;width:100%;height:100%;position:fixed;text-align:left;background:rgba(0,0,0,0.85)}#hellobar-modal .hb-text-wrapper .hb-secondary-text{margin-top:8px}#hellobar-modal .hb-logo-wrapper{margin-top:2.75em;margin-bottom:-2.5em;font-size:0.75em;text-align:center}#hellobar-modal .hb-logo-wrapper.original,#hellobar-modal .hb-logo-wrapper.animated{opacity:0.2}#hellobar-modal .hb-logo-wrapper.original:hover,#hellobar-modal .hb-logo-wrapper.animated:hover{opacity:0.4}#hellobar-modal .hb-logo-wrapper.original svg,#hellobar-modal .hb-logo-wrapper.animated svg{width:3em;height:1.95em;border-radius:3px}#hellobar-modal .hb-logo-wrapper{text-transform:uppercase}#hellobar-modal.top{top:5%}#hellobar-modal.middle{top:50%;transform:translate(-50%, -50%);-o-transform:translate(-50%, -50%);-ms-transform:translate(-50%, -50%);-moz-transform:translate(-50%, -50%);-webkit-transform:translate(-50%, -50%)}#hellobar-modal .icon-close{font-size:14px;top:19px;right:19px}#hellobar-modal .no-thanks-wrapper{text-align:center;padding-top:10px;cursor:pointer}#hellobar-modal .hb-input-wrapper{max-width:22.5em;margin:1.33em auto 0}#hellobar-modal .hb-input-wrapper .hb-cta{margin-top:15px}#hellobar-modal .hb-cta{padding:0;display:flex;align-items:center;justify-content:center}#hellobar-modal .hb-cta .hb-text-holder{border-radius:inherit}#hellobar-modal .hb-input-wrapper .hb-input-block input{text-align:left}#hellobar-modal .hb-inner-content .answer{max-width:540px;margin-left:auto;margin-right:auto;width:100%}#hellobar-modal .gdpr-consent-form{padding-left:45px}#hellobar-modal .gdpr-consent-form p{font-size:16px}#hellobar-modal.image-left .gdpr-consent-form{padding-left:0}#hellobar-modal.image-left .hb-image-wrapper,#hellobar-modal.image-right .hb-image-wrapper{text-align:center}#hellobar-modal.mobile{width:88%;padding:3em 1.25em 1.25em}#hellobar-modal.mobile .hb-logo-wrapper{margin:2em auto 0}#hellobar-modal.mobile .gdpr-consent-form{padding-left:15px}.autodetect #hellobar-modal .answer{padding:10px}.autodetect #hellobar-slider .answer,.autodetect #hellobar-slider .hb-cta{padding-left:8px;padding-right:8px}#hellobar-modal .questionslist{max-width:540px;margin:0 auto}@media screen and (max-width: 840px){#hellobar-modal{width:calc(100% - 20px)}}@media screen and (max-width: 640px){#hellobar-modal .hb-headline-text .fr-view p,#hellobar-takeover .hb-headline-text .fr-view p,#hellobar-modal .hb-secondary-text .fr-view p,#hellobar-takeover .hb-secondary-text .fr-view p{font-size:100%}#hellobar-modal .hb-headline-text .fr-view p span\u003espan.subspan,#hellobar-modal .hb-secondary-text .fr-view p span\u003espan.subspan,#hellobar-modal .hb-headline-text .fr-view p.notedited,#hellobar-modal .hb-secondary-text .fr-view p.notedited,#hellobar-takeover .hb-headline-text .fr-view p span\u003espan.subspan,#hellobar-takeover .hb-secondary-text .fr-view p span\u003espan.subspan,#hellobar-takeover .hb-headline-text .fr-view p.notedited,#hellobar-takeover .hb-secondary-text .fr-view p.notedited{font-size:80%}}\n\n.azuki #hellobar-modal{padding:0 0 30px 0px}.azuki #hellobar-modal .hb-header{display:none}.azuki #hellobar-modal .image-background .hb-image-wrapper.background{height:230px}.azuki #hellobar-modal .image-background .hb-image-wrapper.background ~ .slider-content{margin-top:230px}.azuki #hellobar-modal .hb-image-wrapper.background ~ .hb-content-wrapper{margin-top:230px;display:flex;flex-direction:column}.azuki #hellobar-modal .hb-content-wrapper .hb-inner-content{margin-top:20px}.azuki #hellobar-modal .hb-content-wrapper .hb-image-holder .uploaded-image{max-width:100%;max-height:230px;width:100%;object-fit:cover;margin:0}.azuki #hellobar-modal .hb-text-wrapper{padding:0 2.5em}.azuki #hellobar-modal .hb-text-wrapper .hb-headline-text{font-size:1.50em;font-weight:800;text-transform:uppercase}.azuki #hellobar-modal .hb-input-wrapper{max-width:none;margin:1em auto;padding:0 2.5em}.azuki #hellobar-modal .hb-input-wrapper #hb-fields-form{display:flex;justify-content:space-evenly;align-items:center}.azuki #hellobar-modal .hb-input-wrapper #hb-fields-form\u003e*{margin-left:5px;margin-right:5px}.azuki #hellobar-modal .hb-input-wrapper #hb-fields-form .hb-input-block{margin-bottom:0}.azuki #hellobar-modal .hb-input-wrapper #hb-fields-form .hb-cta{margin-top:0;width:33.3%;flex:0 0 33.3%}.azuki #hellobar-modal .hb-name-input{margin-bottom:5px}.azuki #hellobar-modal .icon-close{top:-24px;right:0;z-index:10000;color:#fff;opacity:1}.azuki #hellobar-modal .hb-image-wrapper{padding:0px;margin-bottom:20px;height:230px;background-position:center}.azuki #hellobar-modal .hb-logo-wrapper{margin-top:1.75em;margin-bottom:-1.5em}.azuki #hellobar-modal .questionslist{display:flex;width:80%;margin:10px auto}.azuki #hellobar-modal .questionslist .hb-cta{width:45% !important;max-width:none;text-transform:uppercase}@media screen and (max-width: 640px){.azuki #hellobar-modal .hb-text-wrapper{padding:0 1.7em}.azuki #hellobar-modal .hb-input-wrapper #hb-fields-form{flex-direction:column;width:85%;margin:0 auto}.azuki #hellobar-modal .hb-input-wrapper #hb-fields-form\u003e*{margin:5px}.azuki #hellobar-modal .hb-input-wrapper #hb-fields-form .hb-input-block{margin-bottom:5px}.azuki #hellobar-modal .hb-input-wrapper #hb-fields-form .hb-cta{margin-top:5px;width:100%;flex:0 0 100%}.azuki #hellobar-modal .questionslist{flex-direction:column;width:85%}.azuki #hellobar-modal .questionslist .hb-cta{margin:5px;width:100% !important}}.azuki #hellobar-takeover .image-background .hb-image-wrapper.background{height:50%}.azuki #hellobar-takeover .image-background .hb-image-wrapper.background ~ .slider-content{margin-top:50%}.azuki #hellobar-takeover .hb-image-wrapper.background ~ .slider-content{margin-top:50%;display:flex;flex-direction:column;padding:15px 25px}.azuki #hellobar-takeover .hb-image-wrapper{padding:0px;margin-bottom:20px;height:50%;background-position:center}.azuki #hellobar-takeover .hb-content-wrapper{top:70%}.azuki #hellobar-takeover .hb-text-wrapper{max-width:540px;margin:0 auto}.azuki #hellobar-takeover .hb-input-wrapper{max-width:540px}.azuki #hellobar-takeover .hb-name-input{margin-bottom:12px}.azuki #hellobar-takeover .hb-header{display:none}@media screen and (max-width: 640px){.azuki #hellobar-takeover{font-size:22px}.azuki #hellobar-takeover .hb-image-wrapper{height:35%}.azuki #hellobar-takeover .hb-content-wrapper{top:65%}}.azuki #hellobar-slider .image-background .hb-image-wrapper.background{height:130px}.azuki #hellobar-slider .image-background .hb-image-wrapper.background ~ .slider-content{margin-top:130px}.azuki #hellobar-slider .hb-image-wrapper.background ~ .slider-content{margin-top:130px;padding:5px 25px}.azuki #hellobar-slider .hb-image-wrapper{padding:0px;margin-bottom:20px;height:130px;background-position:center}.azuki #hellobar-slider .hb-cta{max-width:none}\n","content_upgrades":{},"content_upgrades_styles":{"offer_bg_color":"#ffffb6","offer_text_color":"#000000","offer_link_color":"#1285dd","offer_border_color":"#000000","offer_border_width":"0px","offer_border_style":"solid","offer_border_radius":"0px","modal_button_color":"#1285dd","offer_font_size":"15px","offer_font_weight":"bold","offer_font_family_name":"Open Sans","offer_font_family":"'Open Sans',sans-serif"},"autofills":[],"rules":[{"match":"all","conditions":[{"segment":"pup","operand":"includes","value":["/m/88/","/m/95/","/m/123/","/m/96/","/m/97/","/m/112/","/m/68/","/m/69/","/m/122/","/m/126/","/m/98/","/m/119/","/m/120/","/m/121/"]}],"site_elements":[{"id":666895,"use_question":false,"use_default_image":false,"image_url":"https://s3.amazonaws.com/scripts.hellobar.com/image_uploads/images/000/111/648/modal/Screen_Recording_2019-02-15_at_08.16_PM.gif?1550242048","image_large_url":"https://s3.amazonaws.com/scripts.hellobar.com/image_uploads/images/000/111/648/large/Screen_Recording_2019-02-15_at_08.16_PM.gif?1550242048","image_modal_url":"https://s3.amazonaws.com/scripts.hellobar.com/image_uploads/images/000/111/648/modal/Screen_Recording_2019-02-15_at_08.16_PM.gif?1550242048","image_style":"modal","image_opacity":100,"image_overlay_color":"53847e","image_overlay_opacity":0,"open_in_new_window":false,"primary_color":"FFFFFF","pushes_page_down":true,"remains_at_top":true,"secondary_color":"53847e","settings":{"cookie_settings":{"duration":15,"success_duration":3},"url":"http://dataquest.io","url_to_like":"http://dataquest.io"},"animated":true,"background_color":"FFFFFF","border_color":"53847e","button_color":"53847e","email_placeholder":"Your email","headline":"\u003cp class=\"notedited\"\u003eTERMINAL ISSUE WORKAROUND\u003c/p\u003e","content":"","show_optional_content":false,"show_optional_caption":true,"image_placement":"background","link_color":"FFFFFF","link_text":"GET EARLY ACCESS","name_placeholder":"Your name","placement":"middle","show_border":false,"show_branding":false,"size":"50","text_color":"000000","theme_id":"azuki","type":"Modal","view_condition":"wait-10","wiggle_button":false,"fonts":["open_sans"],"text_field_border_color":"53847e","text_field_border_width":1,"text_field_font_size":14,"text_field_font_family":"open_sans","text_field_border_radius":3,"text_field_text_color":"53847e","text_field_background_color":"FFFFFF","text_field_background_opacity":100,"show_thankyou":false,"conversion_font":"open_sans","conversion_font_color":"53847e","conversion_font_size":18,"show_no_thanks":true,"sound":"none","notification_delay":10,"trigger_color":"374050","trigger_icon_color":"ffffff","enable_gdpr":false,"cta_border_color":"53847e","cta_border_width":0,"cta_border_radius":3,"cta_height":38,"font":"'Open Sans',sans-serif","theme":{"image":{"default_url":"https://assets.hellobar.com/modal-new-default.png","position_default":"background"}},"google_font":"Open+Sans:400,600,700","subtype":"announcement","wiggle_wait":0,"email_redirect":false,"thank_you_text":"Thanks for signing up!","template_name":"modal_announcement","branding_url":"https://www.hellobar.com?sid=666895","closable":false,"use_free_email_default_msg":false,"updated_at":1550247046000.0,"caption":"\u003cp class=\"notedited\"\u003eSome of our students reported that on reaching the end of the terminal they are unable to see the terminal prompt. If you are experiencing this issue just drag the separator to the left as you can see in the above animation.\u003c/p\u003e","views":131,"conversion_rate":0.0}]}],"disable_self_check":false,"modules_version":"47","version":"573b65b5b16279c07b11dd1480d80905dc37a865","timestamp":"2019-03-02T13:35:20.284Z"};var bootstrap=function(t){var e=document,a=e.head||e.getElementsByTagName("head")[0];script=e.createElement("script"),script.async=1,script.src=t,a.appendChild(script)};bootstrap("https://my.hellobar.com/modules-v47.js");