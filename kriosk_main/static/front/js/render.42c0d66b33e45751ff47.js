! function (t) {
	var n = {};

	function e(o) {
		if (n[o]) return n[o].exports;
		var r = n[o] = {
			i: o,
			l: !1,
			exports: {}
		};
		return t[o].call(r.exports, r, r.exports, e), r.l = !0, r.exports
	}
	e.m = t, e.c = n, e.d = function (t, n, o) {
		e.o(t, n) || Object.defineProperty(t, n, {
			enumerable: !0,
			get: o
		})
	}, e.r = function (t) {
		"undefined" !== typeof Symbol && Symbol.toStringTag && Object.defineProperty(t, Symbol.toStringTag, {
			value: "Module"
		}), Object.defineProperty(t, "__esModule", {
			value: !0
		})
	}, e.t = function (t, n) {
		if (1 & n && (t = e(t)), 8 & n) return t;
		if (4 & n && "object" === typeof t && t && t.__esModule) return t;
		var o = Object.create(null);
		if (e.r(o), Object.defineProperty(o, "default", {
				enumerable: !0,
				value: t
			}), 2 & n && "string" != typeof t)
			for (var r in t) e.d(o, r, function (n) {
				return t[n]
			}.bind(null, r));
		return o
	}, e.n = function (t) {
		var n = t && t.__esModule ? function () {
			return t.default
		} : function () {
			return t
		};
		return e.d(n, "a", n), n
	}, e.o = function (t, n) {
		return Object.prototype.hasOwnProperty.call(t, n)
	}, e.p = "https://widget-v4.tidiochat.com/", e.h = "42c0d66b33e45751ff47", e.cn = "render", e(e.s = 213)
}([, , , , , function (t, n) {
	t.exports = function (t, n) {
		if (!(t instanceof n)) throw new TypeError("Cannot call a class as a function")
	}
}, function (t, n) {
	function e(t, n) {
		for (var e = 0; e < n.length; e++) {
			var o = n[e];
			o.enumerable = o.enumerable || !1, o.configurable = !0, "value" in o && (o.writable = !0), Object.defineProperty(t, o.key, o)
		}
	}
	t.exports = function (t, n, o) {
		return n && e(t.prototype, n), o && e(t, o), t
	}
}, , , , , function (t, n, e) {
	"use strict";
	var o = e(12),
		r = e(19),
		i = e(71),
		u = e(23),
		c = e(50),
		a = e(39),
		f = e(72),
		s = e(102),
		d = e(73),
		l = e(20),
		p = e(87),
		v = l("isConcatSpreadable"),
		h = p >= 51 || !r((function () {
			var t = [];
			return t[v] = !1, t.concat()[0] !== t
		})),
		y = d("concat"),
		m = function (t) {
			if (!u(t)) return !1;
			var n = t[v];
			return void 0 !== n ? !!n : i(t)
		};
	o({
		target: "Array",
		proto: !0,
		forced: !h || !y
	}, {
		concat: function (t) {
			var n, e, o, r, i, u = c(this),
				d = s(u, 0),
				l = 0;
			for (n = -1, o = arguments.length; n < o; n++)
				if (i = -1 === n ? u : arguments[n], m(i)) {
					if (l + (r = a(i.length)) > 9007199254740991) throw TypeError("Maximum allowed index exceeded");
					for (e = 0; e < r; e++, l++) e in i && f(d, l, i[e])
				} else {
					if (l >= 9007199254740991) throw TypeError("Maximum allowed index exceeded");
					f(d, l++, i)
				}
			return d.length = l, d
		}
	})
}, function (t, n, e) {
	var o = e(16),
		r = e(55).f,
		i = e(44),
		u = e(49),
		c = e(69),
		a = e(110),
		f = e(85);
	t.exports = function (t, n) {
		var e, s, d, l, p, v = t.target,
			h = t.global,
			y = t.stat;
		if (e = h ? o : y ? o[v] || c(v, {}) : (o[v] || {}).prototype)
			for (s in n) {
				if (l = n[s], d = t.noTargetGet ? (p = r(e, s)) && p.value : e[s], !f(h ? s : v + (y ? "." : "#") + s, t.forced) && void 0 !== d) {
					if (typeof l === typeof d) continue;
					a(l, d)
				}(t.sham || d && d.sham) && i(l, "sham", !0), u(e, s, l, t)
			}
	}
}, , , function (t, n, e) {
	var o = e(23);
	t.exports = function (t) {
		if (!o(t)) throw TypeError(String(t) + " is not an object");
		return t
	}
}, function (t, n, e) {
	(function (n) {
		var e = function (t) {
			return t && t.Math == Math && t
		};
		t.exports = e("object" == typeof globalThis && globalThis) || e("object" == typeof window && window) || e("object" == typeof self && self) || e("object" == typeof n && n) || Function("return this")()
	}).call(this, e(42))
}, , , function (t, n) {
	t.exports = function (t) {
		try {
			return !!t()
		} catch (n) {
			return !0
		}
	}
}, function (t, n, e) {
	var o = e(16),
		r = e(83),
		i = e(27),
		u = e(70),
		c = e(86),
		a = e(115),
		f = r("wks"),
		s = o.Symbol,
		d = a ? s : s && s.withoutSetter || u;
	t.exports = function (t) {
		return i(f, t) || (c && i(s, t) ? f[t] = s[t] : f[t] = d("Symbol." + t)), f[t]
	}
}, , function (t, n) {
	t.exports = !1
}, function (t, n) {
	t.exports = function (t) {
		return "object" === typeof t ? null !== t : "function" === typeof t
	}
}, , , , function (t, n) {
	var e = {}.hasOwnProperty;
	t.exports = function (t, n) {
		return e.call(t, n)
	}
}, , function (t, n, e) {
	var o = e(19);
	t.exports = !o((function () {
		return 7 != Object.defineProperty({}, 1, {
			get: function () {
				return 7
			}
		})[1]
	}))
}, , , function (t, n, e) {
	var o = e(29),
		r = e(97),
		i = e(15),
		u = e(60),
		c = Object.defineProperty;
	n.f = o ? c : function (t, n, e) {
		if (i(t), n = u(n, !0), i(e), r) try {
			return c(t, n, e)
		} catch (o) {}
		if ("get" in e || "set" in e) throw TypeError("Accessors not supported");
		return "value" in e && (t[n] = e.value), t
	}
}, , , , , , function (t, n, e) {
	var o = e(112),
		r = e(16),
		i = function (t) {
			return "function" == typeof t ? t : void 0
		};
	t.exports = function (t, n) {
		return arguments.length < 2 ? i(o[t]) || i(r[t]) : o[t] && o[t][n] || r[t] && r[t][n]
	}
}, function (t, n, e) {
	var o = e(62),
		r = Math.min;
	t.exports = function (t) {
		return t > 0 ? r(o(t), 9007199254740991) : 0
	}
}, , , function (t, n) {
	var e;
	e = function () {
		return this
	}();
	try {
		e = e || new Function("return this")()
	} catch (o) {
		"object" === typeof window && (e = window)
	}
	t.exports = e
}, function (t, n, e) {
	var o = e(80),
		r = e(47);
	t.exports = function (t) {
		return o(r(t))
	}
}, function (t, n, e) {
	var o = e(29),
		r = e(32),
		i = e(56);
	t.exports = o ? function (t, n, e) {
		return r.f(t, n, i(1, e))
	} : function (t, n, e) {
		return t[n] = e, t
	}
}, , , function (t, n) {
	t.exports = function (t) {
		if (void 0 == t) throw TypeError("Can't call method on " + t);
		return t
	}
}, , function (t, n, e) {
	var o = e(16),
		r = e(44),
		i = e(27),
		u = e(69),
		c = e(81),
		a = e(57),
		f = a.get,
		s = a.enforce,
		d = String(String).split("String");
	(t.exports = function (t, n, e, c) {
		var a = !!c && !!c.unsafe,
			f = !!c && !!c.enumerable,
			l = !!c && !!c.noTargetGet;
		"function" == typeof e && ("string" != typeof n || i(e, "name") || r(e, "name", n), s(e).source = d.join("string" == typeof n ? n : "")), t !== o ? (a ? !l && t[n] && (f = !0) : delete t[n], f ? t[n] = e : r(t, n, e)) : f ? t[n] = e : u(n, e)
	})(Function.prototype, "toString", (function () {
		return "function" == typeof this && f(this).source || c(this)
	}))
}, function (t, n, e) {
	var o = e(47);
	t.exports = function (t) {
		return Object(o(t))
	}
}, , function (t, n) {
	var e = {}.toString;
	t.exports = function (t) {
		return e.call(t).slice(8, -1)
	}
}, , , function (t, n, e) {
	var o = e(29),
		r = e(96),
		i = e(56),
		u = e(43),
		c = e(60),
		a = e(27),
		f = e(97),
		s = Object.getOwnPropertyDescriptor;
	n.f = o ? s : function (t, n) {
		if (t = u(t), n = c(n, !0), f) try {
			return s(t, n)
		} catch (e) {}
		if (a(t, n)) return i(!r.f.call(t, n), t[n])
	}
}, function (t, n) {
	t.exports = function (t, n) {
		return {
			enumerable: !(1 & t),
			configurable: !(2 & t),
			writable: !(4 & t),
			value: n
		}
	}
}, function (t, n, e) {
	var o, r, i, u = e(131),
		c = e(16),
		a = e(23),
		f = e(44),
		s = e(27),
		d = e(82),
		l = e(61),
		p = c.WeakMap;
	if (u) {
		var v = new p,
			h = v.get,
			y = v.has,
			m = v.set;
		o = function (t, n) {
			return m.call(v, t, n), n
		}, r = function (t) {
			return h.call(v, t) || {}
		}, i = function (t) {
			return y.call(v, t)
		}
	} else {
		var g = d("state");
		l[g] = !0, o = function (t, n) {
			return f(t, g, n), n
		}, r = function (t) {
			return s(t, g) ? t[g] : {}
		}, i = function (t) {
			return s(t, g)
		}
	}
	t.exports = {
		set: o,
		get: r,
		has: i,
		enforce: function (t) {
			return i(t) ? r(t) : o(t, {})
		},
		getterFor: function (t) {
			return function (n) {
				var e;
				if (!a(n) || (e = r(n)).type !== t) throw TypeError("Incompatible receiver, " + t + " required");
				return e
			}
		}
	}
}, , , function (t, n, e) {
	var o = e(23);
	t.exports = function (t, n) {
		if (!o(t)) return t;
		var e, r;
		if (n && "function" == typeof (e = t.toString) && !o(r = e.call(t))) return r;
		if ("function" == typeof (e = t.valueOf) && !o(r = e.call(t))) return r;
		if (!n && "function" == typeof (e = t.toString) && !o(r = e.call(t))) return r;
		throw TypeError("Can't convert object to primitive value")
	}
}, function (t, n) {
	t.exports = {}
}, function (t, n) {
	var e = Math.ceil,
		o = Math.floor;
	t.exports = function (t) {
		return isNaN(t = +t) ? 0 : (t > 0 ? o : e)(t)
	}
}, , , , , , , function (t, n, e) {
	var o = e(16),
		r = e(44);
	t.exports = function (t, n) {
		try {
			r(o, t, n)
		} catch (e) {
			o[t] = n
		}
		return n
	}
}, function (t, n) {
	var e = 0,
		o = Math.random();
	t.exports = function (t) {
		return "Symbol(" + String(void 0 === t ? "" : t) + ")_" + (++e + o).toString(36)
	}
}, function (t, n, e) {
	var o = e(52);
	t.exports = Array.isArray || function (t) {
		return "Array" == o(t)
	}
}, function (t, n, e) {
	"use strict";
	var o = e(60),
		r = e(32),
		i = e(56);
	t.exports = function (t, n, e) {
		var u = o(n);
		u in t ? r.f(t, u, i(0, e)) : t[u] = e
	}
}, function (t, n, e) {
	var o = e(19),
		r = e(20),
		i = e(87),
		u = r("species");
	t.exports = function (t) {
		return i >= 51 || !o((function () {
			var n = [];
			return (n.constructor = {})[u] = function () {
				return {
					foo: 1
				}
			}, 1 !== n[t](Boolean).foo
		}))
	}
}, , , , , , function (t, n, e) {
	var o = e(62),
		r = Math.max,
		i = Math.min;
	t.exports = function (t, n) {
		var e = o(t);
		return e < 0 ? r(e + n, 0) : i(e, n)
	}
}, function (t, n, e) {
	var o = e(19),
		r = e(52),
		i = "".split;
	t.exports = o((function () {
		return !Object("z").propertyIsEnumerable(0)
	})) ? function (t) {
		return "String" == r(t) ? i.call(t, "") : Object(t)
	} : Object
}, function (t, n, e) {
	var o = e(99),
		r = Function.toString;
	"function" != typeof o.inspectSource && (o.inspectSource = function (t) {
		return r.call(t)
	}), t.exports = o.inspectSource
}, function (t, n, e) {
	var o = e(83),
		r = e(70),
		i = o("keys");
	t.exports = function (t) {
		return i[t] || (i[t] = r(t))
	}
}, function (t, n, e) {
	var o = e(22),
		r = e(99);
	(t.exports = function (t, n) {
		return r[t] || (r[t] = void 0 !== n ? n : {})
	})("versions", []).push({
		version: "3.6.4",
		mode: o ? "pure" : "global",
		copyright: "\xa9 2020 Denis Pushkarev (zloirock.ru)"
	})
}, function (t, n, e) {
	var o = e(113),
		r = e(101).concat("length", "prototype");
	n.f = Object.getOwnPropertyNames || function (t) {
		return o(t, r)
	}
}, function (t, n, e) {
	var o = e(19),
		r = /#|\.prototype\./,
		i = function (t, n) {
			var e = c[u(t)];
			return e == f || e != a && ("function" == typeof n ? o(n) : !!n)
		},
		u = i.normalize = function (t) {
			return String(t).replace(r, ".").toLowerCase()
		},
		c = i.data = {},
		a = i.NATIVE = "N",
		f = i.POLYFILL = "P";
	t.exports = i
}, function (t, n, e) {
	var o = e(19);
	t.exports = !!Object.getOwnPropertySymbols && !o((function () {
		return !String(Symbol())
	}))
}, function (t, n, e) {
	var o, r, i = e(16),
		u = e(116),
		c = i.process,
		a = c && c.versions,
		f = a && a.v8;
	f ? r = (o = f.split("."))[0] + o[1] : u && (!(o = u.match(/Edge\/(\d+)/)) || o[1] >= 74) && (o = u.match(/Chrome\/(\d+)/)) && (r = o[1]), t.exports = r && +r
}, , , , , , , , , function (t, n, e) {
	"use strict";
	var o = {}.propertyIsEnumerable,
		r = Object.getOwnPropertyDescriptor,
		i = r && !o.call({
			1: 2
		}, 1);
	n.f = i ? function (t) {
		var n = r(this, t);
		return !!n && n.enumerable
	} : o
}, function (t, n, e) {
	var o = e(29),
		r = e(19),
		i = e(98);
	t.exports = !o && !r((function () {
		return 7 != Object.defineProperty(i("div"), "a", {
			get: function () {
				return 7
			}
		}).a
	}))
}, function (t, n, e) {
	var o = e(16),
		r = e(23),
		i = o.document,
		u = r(i) && r(i.createElement);
	t.exports = function (t) {
		return u ? i.createElement(t) : {}
	}
}, function (t, n, e) {
	var o = e(16),
		r = e(69),
		i = o["__core-js_shared__"] || r("__core-js_shared__", {});
	t.exports = i
}, function (t, n, e) {
	var o = e(43),
		r = e(39),
		i = e(79),
		u = function (t) {
			return function (n, e, u) {
				var c, a = o(n),
					f = r(a.length),
					s = i(u, f);
				if (t && e != e) {
					for (; f > s;)
						if ((c = a[s++]) != c) return !0
				} else
					for (; f > s; s++)
						if ((t || s in a) && a[s] === e) return t || s || 0;
				return !t && -1
			}
		};
	t.exports = {
		includes: u(!0),
		indexOf: u(!1)
	}
}, function (t, n) {
	t.exports = ["constructor", "hasOwnProperty", "isPrototypeOf", "propertyIsEnumerable", "toLocaleString", "toString", "valueOf"]
}, function (t, n, e) {
	var o = e(23),
		r = e(71),
		i = e(20)("species");
	t.exports = function (t, n) {
		var e;
		return r(t) && ("function" != typeof (e = t.constructor) || e !== Array && !r(e.prototype) ? o(e) && null === (e = e[i]) && (e = void 0) : e = void 0), new(void 0 === e ? Array : e)(0 === n ? 0 : n)
	}
}, , , , , , , , function (t, n, e) {
	var o = e(27),
		r = e(111),
		i = e(55),
		u = e(32);
	t.exports = function (t, n) {
		for (var e = r(n), c = u.f, a = i.f, f = 0; f < e.length; f++) {
			var s = e[f];
			o(t, s) || c(t, s, a(n, s))
		}
	}
}, function (t, n, e) {
	var o = e(38),
		r = e(84),
		i = e(114),
		u = e(15);
	t.exports = o("Reflect", "ownKeys") || function (t) {
		var n = r.f(u(t)),
			e = i.f;
		return e ? n.concat(e(t)) : n
	}
}, function (t, n, e) {
	var o = e(16);
	t.exports = o
}, function (t, n, e) {
	var o = e(27),
		r = e(43),
		i = e(100).indexOf,
		u = e(61);
	t.exports = function (t, n) {
		var e, c = r(t),
			a = 0,
			f = [];
		for (e in c) !o(u, e) && o(c, e) && f.push(e);
		for (; n.length > a;) o(c, e = n[a++]) && (~i(f, e) || f.push(e));
		return f
	}
}, function (t, n) {
	n.f = Object.getOwnPropertySymbols
}, function (t, n, e) {
	var o = e(86);
	t.exports = o && !Symbol.sham && "symbol" == typeof Symbol.iterator
}, function (t, n, e) {
	var o = e(38);
	t.exports = o("navigator", "userAgent") || ""
}, , , , , , , , , , , , , , function (t, n, e) {
	(function (t) {
		("undefined" !== typeof window ? window : "undefined" !== typeof t ? t : "undefined" !== typeof self ? self : {}).SENTRY_RELEASE = {
			id: "1.48.0"
		}
	}).call(this, e(42))
}, function (t, n, e) {
	var o = e(16),
		r = e(81),
		i = o.WeakMap;
	t.exports = "function" === typeof i && /native code/.test(r(i))
}, , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , function (t, n, e) {
	e(130), t.exports = e(214)
}, function (t, n, e) {
	"use strict";
	e.r(n);
	e(11);
	! function () {
		var t = e(215).default,
			n = "boolean" === typeof PRODUCTION_DEVELOPMENT_BUILD && !0 === PRODUCTION_DEVELOPMENT_BUILD,
			o = function () {
				var t = [],
					n = !1,
					e = !1;

				function o() {
					if (!n) {
						n = !0;
						for (var e = 0; e < t.length; e += 1) t[e].fn.call(window, t[e].ctx);
						t = []
					}
				}

				function r() {
					"complete" === document.readyState && o()
				}
				return function (i, u) {
					if ("function" !== typeof i) throw new TypeError("callback for docReady(fn) must be a function");
					return n ? (setTimeout((function () {
						i(u)
					}), 1), !1) : (t.push({
						fn: i,
						ctx: u
					}), "complete" === document.readyState || !document.attachEvent && "interactive" === document.readyState ? setTimeout(o, 1) : e || (document.addEventListener ? (document.addEventListener("DOMContentLoaded", o, !1), window.addEventListener("load", o, !1)) : (document.attachEvent("onreadystatechange", r), window.attachEvent("onload", o)), e = !0), !0)
				}
			}();
		window.tidioChatApi = new t, o((function () {
			var t = window.document.getElementById("tidio-chat-code"),
				o = window.Shopify && !0 === window.Shopify.designMode;
			if (t || o) return !1;
			! function (t, n, e) {
				var o = n.createElement("iframe"),
					r = !1;
				o.onload = function () {
					r || (e(o), r = !0)
				}, o.id = t, o.style.display = "none", o.title = "Tidio Chat code", n.body.appendChild(o), setTimeout((function () {
					r || (e(o), r = !0)
				}), 1e3)
			}("tidio-chat-code", window.document, (function (t) {
				n && window.__REDUX_DEVTOOLS_EXTENSION__ && (t.contentWindow.__REDUX_DEVTOOLS_EXTENSION__ = window.__REDUX_DEVTOOLS_EXTENSION__, t.contentWindow.__REDUX_DEVTOOLS_EXTENSION_COMPOSE__ = window.__REDUX_DEVTOOLS_EXTENSION_COMPOSE__), t.contentWindow.tidioChatApi = window.tidioChatApi;
				var o = n ? "".concat("https://widget-v4.tidiochat.com/", "/dist/") : "https://widget-v4.tidiochat.com/";
				! function (t, n) {
					var e = t.contentWindow.document,
						o = e.createElement("script");
					o.src = n, o.async = !0, e.body.appendChild(o)
				}(t, "".concat(o, "/").concat("1_48_0", "/static/js/widget.").concat(e.h, ".js"))
			}))
		}))
	}()
}, function (t, n, e) {
	"use strict";
	e.r(n), e.d(n, "default", (function () {
		return c
	}));
	e(11);
	var o = e(5),
		r = e.n(o),
		i = e(6),
		u = e.n(i),
		c = function () {
			function t() {
				r()(this, t), this.eventPrefix = "tidioChat-", this.readyEventWasFired = !1, this.queue = [], this.popUpOpen = this.open, this.popUpHide = this.close, this.chatDisplay = this.display, this.setColorPallete = this.setColorPalette
			}
			return u()(t, [{
				key: "on",
				value: function (t, n) {
					"ready" === t && this.readyEventWasFired ? n() : document.addEventListener("".concat(this.eventPrefix).concat(t), (function (t) {
						n(t.data)
					}), !1)
				}
			}, {
				key: "trigger",
				value: function (t, n) {
					if ("ready" === t && this.readyEventWasFired) return !1;
					try {
						var e = document.createEvent("Event");
						if (e.initEvent("".concat(this.eventPrefix).concat(t), !0, !0), e.data = n, document.dispatchEvent(e), "ready" === t) {
							if (this.readyEventWasFired) return !1;
							this._flushAllFromQueue(), this.readyEventWasFired = !0
						}
					} catch (o) {
						return !1
					}
					return !0
				}
			}, {
				key: "method",
				value: function (t, n) {
					return "ready" === t && "function" === typeof n ? (this.on("ready", n), !0) : (this[t] && this[t](n), !0)
				}
			}, {
				key: "_addToQueue",
				value: function (t) {
					var n = arguments.length > 1 && void 0 !== arguments[1] ? arguments[1] : null;
					this.queue.push({
						method: t,
						args: n
					})
				}
			}, {
				key: "_flushAllFromQueue",
				value: function () {
					for (; 0 !== this.queue.length;) {
						var t = this.queue.shift(),
							n = t.method,
							e = t.args;
						this[n].apply(null, e)
					}
				}
			}, {
				key: "open",
				value: function () {
					this._addToQueue("open")
				}
			}, {
				key: "close",
				value: function () {
					this._addToQueue("close")
				}
			}, {
				key: "display",
				value: function () {
					var t = !(arguments.length > 0 && void 0 !== arguments[0]) || arguments[0];
					this._addToQueue("display", [t])
				}
			}, {
				key: "show",
				value: function () {
					this._addToQueue("show")
				}
			}, {
				key: "hide",
				value: function () {
					this._addToQueue("hide")
				}
			}, {
				key: "setColorPalette",
				value: function (t) {
					this._addToQueue("setColorPalette", [t])
				}
			}, {
				key: "track",
				value: function () {
					var t = arguments.length > 0 && void 0 !== arguments[0] ? arguments[0] : "track",
						n = arguments.length > 1 && void 0 !== arguments[1] ? arguments[1] : {},
						e = arguments.length > 2 && void 0 !== arguments[2] ? arguments[2] : function () {};
					this._addToQueue("track", [t, n, e])
				}
			}, {
				key: "messageFromVisitor",
				value: function (t) {
					this._addToQueue("messageFromVisitor", [t])
				}
			}, {
				key: "messageFromOperator",
				value: function (t) {
					var n = !(arguments.length > 1 && void 0 !== arguments[1]) || arguments[1];
					this._addToQueue("messageFromOperator", [t, n])
				}
			}, {
				key: "setVisitorData",
				value: function (t, n) {
					this._addToQueue("setVisitorData", [t, n])
				}
			}, {
				key: "setContactProperties",
				value: function (t, n) {
					this._addToQueue("setContactProperties", [t, n])
				}
			}, {
				key: "addVisitorTags",
				value: function (t, n) {
					this._addToQueue("addVisitorTags", [t, n])
				}
			}, {
				key: "setFeatures",
				value: function () {
					var t = arguments.length > 0 && void 0 !== arguments[0] ? arguments[0] : {};
					this._addToQueue("setFeatures", t)
				}
			}]), t
		}()
}]);