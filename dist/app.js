(()=>{"use strict";function e(t){return e="function"==typeof Symbol&&"symbol"==typeof Symbol.iterator?function(e){return typeof e}:function(e){return e&&"function"==typeof Symbol&&e.constructor===Symbol&&e!==Symbol.prototype?"symbol":typeof e},e(t)}function t(e){return function(e){if(Array.isArray(e))return i(e)}(e)||function(e){if("undefined"!=typeof Symbol&&Symbol.iterator in Object(e))return Array.from(e)}(e)||n(e)||function(){throw new TypeError("Invalid attempt to spread non-iterable instance.\nIn order to be iterable, non-array objects must have a [Symbol.iterator]() method.")}()}function n(e,t){if(e){if("string"==typeof e)return i(e,t);var n=Object.prototype.toString.call(e).slice(8,-1);return"Object"===n&&e.constructor&&(n=e.constructor.name),"Map"===n||"Set"===n?Array.from(e):"Arguments"===n||/^(?:Ui|I)nt(?:8|16|32)(?:Clamped)?Array$/.test(n)?i(e,t):void 0}}function i(e,t){(null==t||t>e.length)&&(t=e.length);for(var n=0,i=new Array(t);n<t;n++)i[n]=e[n];return i}function r(e,t){var n=arguments.length>2&&void 0!==arguments[2]&&arguments[2];return n?f(e)?t:e:m(e)?t:e}function a(e){return u(e)&&0===e.length}function l(e){return"string"==typeof e||e instanceof String}function o(e){return"function"==typeof e}function s(t){return!m(t)&&"object"===e(t)}function u(e){return!m(e)&&"function"==typeof e[Symbol.iterator]}function c(e){return u(e)&&!l(e)}function d(e){return null===e}function h(e){return!e||l(e)&&(0===e.length||/^\s*$/.test(e))}function f(e){return void 0===e}function m(e){return d(e)||f(e)}var p=Object.prototype.hasOwnProperty,b=(Object.prototype.isPrototypeOf,function(e,t){return p.call(e,t)});var g=function(e){return!m(e)&&e.nodeType===Node.ELEMENT_NODE},v=function(e){return e instanceof Node},y=function(e){return g(e)&&e instanceof Element},C=function(e,t){return!!(g(e)&&e instanceof HTMLElement)&&(!u(t)||(i=e,r=Array.isArray(t)?t:[t],l=function(e){return i instanceof e},o=function(e){return i.tagName===e.toUpperCase()},s=function(e){return Array.isArray(e)?e.includes(i.type):i.type===e},r.some((function(e){if(!u(e))return!1;var t,i,r=e,d=null;if(Array.isArray(e)){var f=(i=2,function(e){if(Array.isArray(e))return e}(t=e)||function(e,t){if("undefined"!=typeof Symbol&&Symbol.iterator in Object(e)){var n=[],i=!0,r=!1,a=void 0;try{for(var l,o=e[Symbol.iterator]();!(i=(l=o.next()).done)&&(n.push(l.value),!t||n.length!==t);i=!0);}catch(e){r=!0,a=e}finally{try{i||null==o.return||o.return()}finally{if(r)throw a}}return n}}(t,i)||n(t,i)||function(){throw new TypeError("Invalid attempt to destructure non-iterable instance.\nIn order to be iterable, non-array objects must have a [Symbol.iterator]() method.")}());r=f[0],d=f[1]}r=r.toLowerCase();var m,p="HTML".concat(b(E,r)?E[r]:h(m=r)?m:function(e){return h(e)?e:e.toLowerCase().replace(/\b\w/g,(function(e){return e.toUpperCase()}))}(m.replace(/[_-]+/g," ").replace(/\s+/g," ").trim()).replace(/\s+/g,""),"Element");return!(!l(window[p])&&!o(r))&&(!(c(d)&&!a(d))||s(d))}))));var i,r,l,o,s},E={a:"Anchor",br:"BR",dl:"DList",datalist:"DataList",fieldset:"FieldSet",frameset:"FrameSet",hr:"HR",h1:"Heading",h2:"Heading",h3:"Heading",h4:"Heading",h5:"Heading",h6:"Heading",li:"LI",ol:"OList",optgroup:"OptGroup",p:"Paragraph",q:"Quote",blockquote:"Quote",caption:"TableCaption",td:"TableCell",th:"TableCell",col:"TableCol",tr:"TableRow",tbody:"TableSection",thead:"TableSection",tfoot:"TableSection",textarea:"TextArea",ul:"UList"},w=function(e){return function(e){return!m(e)&&e.nodeType===Node.DOCUMENT_FRAGMENT_NODE}(e)&&e instanceof DocumentFragment};function A(e,t){if(!l(t))return null;var n=document.createElement("template");return n.innerHTML=t.trim(),n.content[e]}var S=A.bind(null,"firstChild");function k(e,t,n){e[t]=n}function T(e,t,n){e.setAttribute(t,n)}A.bind(null,"childNodes");var I="accesskey,autocapitalize,class,dataset,editable,draggable,hidden,id,inputmode,lang,html,style,tabindex,text,title",L={accesskey:[k,"accessKey"],autocapitalize:[k,"autocapitalize"],class:[function(e,n){var i;if(!C(e))throw new Error("Bad argument: The passed `element` argument is not a valid HTML Element");return(i=e.classList).add.apply(i,t(Array.isArray(n)?n:[n])),e}],dataset:[function(e,t,n){Object.assign(e[t],n)},"dataset"],draggable:[k,"draggable"],editable:[k,"contentEditable"],hidden:[k,"hidden"],id:[k,"id"],inputmode:[k,"inputMode"],lang:[k,"lang"],html:[k,"innerHTML"],style:[k,"style"],tabindex:[k,"tabIndex"],text:[k,"textContent"],title:[k,"title"],data:[k,"data"],cite:[k,"cite"],download:[k,"download"],ping:[k,"ping"],target:[k,"target"],coords:[k,"coords"],shape:[k,"shape"],autoplay:[k,"autoplay"],buffered:[k,"buffered"],controls:[k,"controls"],loop:[k,"loop"],muted:[k,"muted"],playsinline:[T,"playsinline"],poster:[k,"poster"],preload:[k,"preload"],crossorigin:[k,"crossOrigin"],decoding:[k,"decoding"],height:[k,"height"],ismap:[k,"isMap"],loading:[k,"loading"],srcset:[k,"srcset"],width:[k,"width"],alt:[k,"alt"],as:[k,"as"],media:[k,"media"],rel:[k,"rel"],src:[k,"src"],sizes:[k,"sizes"],reversed:[k,"reversed"],start:[k,"start"],accept:[k,"accept"],"accept-charset":[k,"acceptCharset"],action:[k,"action"],autocomplete:[k,"autocomplete"],autofocus:[k,"autofocus"],capture:[k,"capture"],checked:[k,"checked"],cols:[k,"cols"],disabled:[k,"disabled"],dirname:[k,"dirName"],enctype:[k,"enctype"],for:[k,"for"],form:[k,"form"],formaction:[k,"formAction"],formenctype:[k,"formEnctype"],formmethod:[k,"formMethod"],formnovalidate:[k,"formNoValidate"],formtarget:[k,"formTarget"],high:[k,"high"],label:[k,"label"],list:[k,"list"],low:[k,"low"],max:[k,"max"],maxlength:[k,"maxLength"],method:[k,"method"],min:[k,"min"],minlength:[k,"minLength"],multiple:[k,"multiple"],name:[k,"name"],novalidate:[k,"noValidate"],optimum:[k,"optimum"],pattern:[k,"pattern"],placeholder:[k,"placeholder"],readonly:[k,"readOnly"],required:[k,"required"],rows:[k,"rows"],selected:[k,"selected"],size:[k,"size"],spellcheck:[T,"spellcheck"],step:[k,"step"],wrap:[k,"wrap"],default:[k,"default"],kind:[k,"kind"],srclang:[k,"srclang"],abbr:[k,"abbr"],colspan:[k,"colSpan"],span:[k,"span"],rowspan:[k,"rowSpan"],scope:[k,"scope"],href:[k,"href"],hreflang:[k,"hreflang"],datetime:[k,"dateTime"],type:[k,"type"],value:[k,"value"],usemap:[k,"useMap"]};function O(e,n,i){var a=document.createElement(e);return C(a)?(s(i)&&function(e,n){var i=arguments.length>2&&void 0!==arguments[2]?arguments[2]:"";if(!C(e))throw new Error("Bad argument: The given element argument is not a valid HTML Element");if(!s(n))return e;for(var r=function(e){return I.includes(e)||i.includes(e)},a=0,l=Object.keys(n);a<l.length;a++){var o=l[a];if(r(o)){var u=n[o],c=L[o].slice(0);c.shift().apply(void 0,[e].concat(t(c),[u]))}}}(a,i,r(n,"")),a):null}function x(e,t,n,i){var r=O(e,t,n);return C(r)?(m(i)||F(r,i),r):null}function M(e,t,n,i,r){var a=O(e,t,i);return C(a)?(m(r)||F(a,r,n),a):null}O.bind(null,"link","as,crossorigin,disabled,href,hreflang,media,rel,sizes,type"),x.bind(null,"template",""),x.bind(null,"header",""),x.bind(null,"footer",""),x.bind(null,"main",""),x.bind(null,"article",""),x.bind(null,"section",""),x.bind(null,"nav",""),x.bind(null,"aside",""),x.bind(null,"h1",""),x.bind(null,"h2",""),x.bind(null,"h3",""),x.bind(null,"h4",""),x.bind(null,"h5",""),x.bind(null,"h6",""),x.bind(null,"div",""),x.bind(null,"object","data,height,name,type,usemap,width"),O.bind(null,"embed","height,src,type,width"),O.bind(null,"br",""),O.bind(null,"hr",""),x.bind(null,"p",""),x.bind(null,"blockquote","cite");var j=function(e){return C(e,"li")?e:N(null,e)},N=(M.bind(null,"ul","",j),M.bind(null,"ol","reversed,start,type",j),x.bind(null,"li","value")),H=(x.bind(null,"dl",""),x.bind(null,"dt",""),x.bind(null,"dd",""),x.bind(null,"a","download,href,hreflang,ping,rel,target,type"),O.bind(null,"area","alt,coords,download,href,hreflang,media,ping,rel,shape,target"),O.bind(null,"base","href,target"),O.bind(null,"img","alt,crossorigin,decoding,height,ismap,loading,sizes,src,srcset,usemap,width"),x.bind(null,"audio","autoplay,controls,crossorigin,loop,muted,preload,src"),x.bind(null,"video","autoplay,controls,crossorigin,height,loop,muted,playsinline,poster,preload,src,width"),O.bind(null,"source","media,sizes,src,srcset,type"),O.bind(null,"track","default,kind,label,src,srclang"),x.bind(null,"picture",""),x.bind(null,"figure",""),x.bind(null,"figcaption",""),x.bind(null,"span",""),x.bind(null,"strong",""),x.bind(null,"em",""),x.bind(null,"mark",""),x.bind(null,"samp",""),x.bind(null,"sub",""),x.bind(null,"sup",""),x.bind(null,"del","cite,datetime"),x.bind(null,"ins","cite,datetime"),x.bind(null,"q","cite"),x.bind(null,"abbr",""),x.bind(null,"b",""),x.bind(null,"i",""),x.bind(null,"s",""),x.bind(null,"u",""),x.bind(null,"cite",""),x.bind(null,"time","datetime"),x.bind(null,"code",""),x.bind(null,"form","accept-charset,action,autocomplete,enctype,method,name,novalidate,rel,target"),O.bind(null,"input","accept,alt,autocomplete,autofocus,capture,checked,dirname,disabled,height,max,maxlength,minlength,min,multiple,name,pattern,placeholder,readonly,required,size,src,step,type,value,width"),x.bind(null,"textarea","autocomplete,autofocus,cols,disabled,maxlength,minlength,name,placeholder,readonly,required,rows,spellcheck,value,wrap"),x.bind(null,"label","for"),M.bind(null,"select","autocomplete,autofocus,disabled,multiple,name,required,size",(function(e){return C(e,["option","optgroup"])?e:Array.isArray(e)?z(null,e):H(null,e)})),x.bind(null,"option","disabled,label,selected,value")),_=function(e){return C(e,"option")?e:H(null,e)},z=M.bind(null,"optgroup","disabled,label",_),B=(x.bind(null,"fieldset","disabled,name"),x.bind(null,"legend",""),M.bind(null,"datalist","",_),x.bind(null,"meter","high,low,max,min,optimum,value"),x.bind(null,"progress","max,value"),x.bind(null,"output","name,value"),x.bind(null,"button","autofocus,disabled,formaction,formenctype,formmethod,formnovalidate,formtarget,name,type,value"),x.bind(null,"table",""),x.bind(null,"caption",""),function(e){return C(e,"tr")?e:q(null,e)}),q=(M.bind(null,"thead","",B),M.bind(null,"tbody","",B),M.bind(null,"tfoot","",B),O.bind(null,"col","span"),M.bind(null,"colgroup","span",(function(e){return C(e,"col")?e:null})),M.bind(null,"tr","",(function(e){return C(e,["th","td"])?e:D(null,e)}))),D=(x.bind(null,"th","abbr,colspan,rowspan,scope"),x.bind(null,"td","colspan,rowspan"));function F(e,t,n){var i=Array.isArray(t)?t:[t];return o(n)&&(i=i.map((function(e){return n(e)}))),function(e,t){if(!v(e))throw new TypeError("Bad argument: The given `parent` is not a valid Node");if(!(t instanceof HTMLCollection||c(t)))throw new TypeError("Bad argument: The given `children` is not a valid HTMLCollection/HTMLElement array");var n=w(e)?e:document.createDocumentFragment();Array.from(t).forEach((function(e){var t;m(e)||n.appendChild(v(e)?e:(t=e.toString(),document.createTextNode(t.toString())))})),e!==n&&e.appendChild(n)}(e,i),e}var R=function(e){return/^\.[a-zA-Z0-9_-]+$/.test(e)};function U(e,t){var n=r(t,document);return h(e)?null:w(n)?n.querySelector(e):function(e){return/^#[a-zA-Z0-9_-]+$/.test(e)}(e)?document.getElementById(e.substring(1)):R(e)?n.getElementsByClassName(e.substring(1))[0]:n.querySelector(e)}function V(e,t){var n=r(t,document);return h(e)?null:w(n)?n.querySelectorAll(e):R(e)?n.getElementsByClassName(e.substring(1)):n.querySelectorAll(e)}function P(e,t){return"content"in document.createElement("template")?U(e,t):null}function G(e,t,n){if(!C(t))return null;var i=t[e];if(o(n))for(;y(i)&&!n(i);)i=i[e];return i}function Q(e,t,n){if(!y(e))throw new TypeError("Bad argument: The given target parameter is not a valid HTML Element");if(!o(t))throw new TypeError("Bad argument: The given pred parameter is not a valid Function");var i=e.parentElement;return n>0?K(i,t,n-1):$(i,t)}function $(e,t){return m(e)?null:t(e)?e:$(e.parentElement,t)}function K(e,t,n){return m(e)||0===n?null:t(e)?e:K(e.parentElement,t,n-1)}G.bind(null,"previousElementSibling"),G.bind(null,"nextElementSibling");var Z="state",J=function(e){return e.dataset[Z]},X=function(e,t){return e.dataset[Z]=t},W=function(e,t){return X(e,r(t,"checked"))},Y=function(e,t){return X(e,r(t,"unchecked"))};function ee(e,t,n){if(C(e))return t(e)?[e]:V(n,e);if(l(e)&&!a(e)){var i=U(e);return m(i)?null:ee(i)}return m(e)?V(n):null}var te={name:"form-selector",container:null,items:null,selectedIndex:null,selectedItem:null,beforeChange:null,afterChange:null,get value(){return this.selectedItem.value},setSelectedItem:function(e){return this.items.includes(e)?(this.selectedItem&&this.selectedItem.setChecked(!1),this.selectedItem=e,this.selectedItem.setChecked(!0),!0):null},init:function(){for(var e=this.container.dataset.value,t=null,n=0;n<this.items.length;n++){var i=this.items[n];i.isChecked()&&this.setSelectedItem(i),i.value===e&&(t=i)}return d(this.selectedItem)&&!d(t)&&this.setSelectedItem(t),this.bindEvents(),this},bindEvents:function(){var e=this;this.container.addEventListener("change",(function(t){var n=t.target,i=!1;if(o(e.beforeChange)&&(i=!1===e.beforeChange(e,t)),i)return n.checked=!1,void e.items[e.selectedIndex].setChecked(!0);var a=e.items.find((function(e){return e.index===+r(n.dataset.selectorIndex,-1)}));m(a)||(e.setSelectedItem(a),o(e.afterChange)&&e.afterChange(e,t))}))}},ne=function(e){return'[data-type="'.concat(e.name,'"]')},ie={BaseSelector:ne({name:"selector",container:null,items:null,selectedIndex:null,selectedItem:null,beforeChange:null,afterChange:null,get value(){return this.selectedItem.value},setSelectedItem:function(e){return this.items.includes(e)?(this.selectedItem&&this.selectedItem.setChecked(!1),this.selectedItem=e,this.selectedItem.setChecked(!0),!0):null},init:function(){for(var e=this.container.dataset.value,t=null,n=0;n<this.items.length;n++){var i=this.items[n];i.isChecked()&&this.setSelectedItem(i),i.value===e&&(t=i)}return d(this.selectedItem)&&!d(t)&&this.setSelectedItem(t),this.bindEvents(),this},bindEvents:function(){var e=this;this.container.addEventListener("click",(function(t){var n=t.target;if(b(n.dataset,"selector")){var i=!1;if(o(e.beforeChange)&&(i=!1===e.beforeChange(e,t)),!i){var a=e.items.find((function(e){return e.index===+r(n.dataset.selectorIndex,-1)}));m(a)||(e.setSelectedItem(a),o(e.afterChange)&&e.afterChange(e,t))}}}))}}),FormSelector:ne(te)};new Error("Missing container: A selector requires a container"),new Error("Missing input: FormSelector requires an input in the container"),[ie.BaseSelector,ie.FormSelector].join(","),new Error("Missing container: A switch requires a container"),new Error("Missing input: FormSwitch requires an input in the container");var re="on",ae=function(e){return'[data-type="'.concat(e.name,'"]')},le={name:"form-switch",container:null,input:null,beforeChange:null,afterChange:null,get value(){return this.input.value},isChecked:function(){return J(this.container)===re},setChecked:function(e){return!m(e)&&(this.input.checked=e,e?W(this.container,re):Y(this.container,"off"),!0)},toggle:function(){this.isChecked()?this.setChecked(!1):this.setChecked(!0)},init:function(e){return Object.assign(this,e),this.input.checked&&this.setChecked(!0),this.bindEvents(),this},bindEvents:function(){var e=this;this.input.addEventListener("change",(function(t){var n=!1;o(e.beforeChange)&&(n=!1===e.beforeChange(e,t)),n?e.input.checked=!e.input.checked:(e.toggle(),o(e.afterChange)&&e.afterChange(e,t))}))}};function oe(e){e.style.display="block"}function se(e){e.style.display="none"}[ae({name:"switch",container:null,beforeChange:null,afterChange:null,get value(){return this.container.dataset.value},isChecked:function(){return J(this.container)===re},setChecked:function(e){return!m(e)&&(e?W(this.container,re):Y(this.container,"off"),!0)},toggle:function(){this.isChecked()?this.setChecked(!1):this.setChecked(!0)},init:function(e){return Object.assign(this,e),this.isChecked()&&W(this.container,re),this.bindEvents(),this},bindEvents:function(){var e=this;this.container.addEventListener("click",(function(t){var n=!1;o(e.beforeChange)&&(n=!1===e.beforeChange(e,t)),n||(e.toggle(),o(e.afterChange)&&e.afterChange(e,t))}))}}),ae(le)].join(",");var ue="BAD_CONTAINER_COLLAPSIBLE",ce={BAD_CONTAINER_COLLAPSIBLE:new Error("Missing container: A collapsible requires a container"),BAD_CONTAINER_ACCORDION:new Error("Missing container: An accordion requires a container")},de="expanded",he="collapsed",fe=function(e){return"collapsible"in e.dataset},me={create:function(e,t){if(!C(e))return ue;var n=Object.create(this);return Object.assign(n,t,{container:e}),n},name:"collapsible",container:null,header:null,content:null,beforeOpen:null,afterOpen:null,beforeClose:null,afterClose:null,getState:function(){return this.container.dataset[this.name]},setState:function(e){this.container.dataset[this.name]=e},isCollapsed:function(){return this.getState()===he},isExpanded:function(){return this.getState()===de},isClosed:!1,isInitialized:!1,open:function(){if(this.isInitialized&&!this.isClosed)return this;var e=!1;return o(this.beforeOpen)&&(e=!1===this.beforeOpen(this)),e||(this.toggle(oe,de,"add"),o(this.afterOpen)&&this.afterOpen(this),this.isClosed=!1),this},close:function(){if(this.isInitialized&&this.isClosed)return this;var e=!1;return o(this.beforeClose)&&(e=!1===this.beforeClose(this)),e||(this.toggle(se,he,"remove"),o(this.afterClose)&&this.afterClose(this),this.isClosed=!0),this},toggle:function(e,t,n){e(this.content),this.setState(t),this.container.classList[n]("expanded")},init:function(e){return Object.assign(this,e),this.header=U("[data-".concat(this.name,"-header]"),this.container),this.content=U("[data-".concat(this.name,"-content]"),this.container),this.isCollapsed()?this.close():this.isExpanded()&&(this.isClosed=!0,this.open()),this.bindEvents(),this.isInitialized=!0,this},bindEvents:function(){var e=this,t=this.container,n=this.header;n.addEventListener("click",(function(i){var r=Q(i.target,(function(t){return e.name in t.dataset}));t===r&&(e.isCollapsed()?e.open():n.parentNode===t&&e.close())}))}};encodeURIComponent;const pe=[{name:"Louis-Edouard LAFONTANT",role:"instructor",title:"Chargé de cours",local:"Bureau 2352 Pav. André-Aisenstadt",web:"http://www-ens.iro.umontreal.ca/~lafontle/",photo:"./assets/images/photo_louis_edouard_lafontant.jpeg",email:"louis.edouard.lafontant@umontreal.ca",intro:'Envoyez-moi vos messages par <a href="mailto:louis.edouard.lafontant@umontreal.ca">courriel</a> ou via Discord (<b>L-E#2545</b>). Pour planifier une rencontre, utilisez le <a href="https://calendly.com/lelafontant/ift1015-periode-de-consultation">calendrier</a>.'},{name:"Hajer MEJRI",role:"assistant",title:"Auxiliaire d'enseignement",local:"À venir",web:"https://www.linkedin.com/in/hajer-mejri-45431b140",photo:"https://media.licdn.com/dms/image/C4E03AQFKeufvFVSogg/profile-displayphoto-shrink_400_400/0/1643236712169?e=1678924800&v=beta&t=ST4kQEN-GMejEe4S1_LVA492tljLe9HUsx7XXfSodkQ",email:"hajer.mejri.1@umontreal.ca",intro:'Envoyez-moi vos messages par <a href="mailto:hajer.mejri.1@umontreal.ca">courriel</a> ou via Discord (<b>Hajer#6578</b>).'},{name:"Hassan ABASS",role:"assistant",title:"Auxiliaire d'enseignement",local:"À venir",web:"https://www.linkedin.com/in/hassan-abass-7552261b7",photo:"https://media.licdn.com/dms/image/D4E03AQHlDyKSVv3fpw/profile-displayphoto-shrink_400_400/0/1664379672955?e=1678924800&v=beta&t=HUasi2Ju09OQBgsg8-JruyB3PvxEryZqoGuxNSOMnaE",email:"hassan.abass@umontreal.ca",intro:'Envoyez-moi vos messages par <a href="mailto:hassan.abass@umontreal.ca">courriel</a> ou via Discord (<b>flatcaphat#1289</b>).'},{name:"Amélie Thérèse COUGHLAN",role:"assistant",title:"Auxiliaire d'enseignement",local:"À venir",web:"linkedin.com/in/amélie-coughlan-2a883a22b",photo:"https://media.licdn.com/dms/image/D4E03AQGRoeIwuV_yVA/profile-displayphoto-shrink_400_400/0/1666487427401?e=1679529600&v=beta&t=kUD6CTFKPjVkZV5GAMX3uMoSVcao_nSv7rGUBqeDs7c",email:"amelie.therese.coughlan@umontreal.ca",intro:'Envoyez-moi vos messages par <a href="mailto:amelie.therese.coughlan@umontreal.ca">courriel</a> ou via Discord (<b>roasteddino#0638</b>).'}];let be=U(".body-content"),ge=U('[data-name="teachers"]'),ve=(V('[data-name="schedule"]'),U('[data-name="weeks"]'));if(ge){let e=P("#tpl-teacher").innerHTML;pe.forEach((t=>{let n=S(Ce(e,t));ge.append(n)}))}if(ve){let e=P("#tpl-week").innerHTML;WEEK_DATA.forEach((t=>{let n=S(Ce(e,t));ye(n,t),ve.append(n)}))}function ye(e,t){V("[data-item]",e).forEach((e=>{const{item:n,bind:i}=e.dataset;let r=t[i],a=P(`#${n}`).innerHTML;r.forEach((t=>{let n=S(Ce(a,t));V("[data-item]",n)&&ye(n,t),e.append(n)}))}))}function Ce(e,t){var n=e.trim();let i=n.match(/(\$value)/g);i&&i.forEach(((e,i)=>{n=n.replace(e,t)}));let r=n.match(/(#[A-Za-z0-9_]+)/g);return r&&r.forEach(((e,i)=>{let r=e.substring(1);b(t,r)&&(n=n.replace(e,t[r]))})),n}!function(e,t){var n=ee(e,fe,"[data-collapsible]"),i=r(void 0,{});if(m(n))return null;for(var a=[],l=0;l<n.length;l++){var o=me.create(n[l],i);if(b(ce,o))throw ce[o];o.init(),a.push(o)}}(be)})();