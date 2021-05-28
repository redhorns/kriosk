jQuery((function (t) {
	function i() {
		void 0 !== t.fn.selectBox && t("select.selectBox").filter(":visible").not(".enhanced").selectBox().addClass("enhanced")
	}

	function e() {
		if (void 0 !== t.prettyPhoto) {
			var e = {
				hook: "data-rel",
				social_tools: !1,
				theme: "pp_woocommerce",
				horizontal_padding: 20,
				opacity: .8,
				deeplinking: !1,
				overlay_gallery: !1,
				default_width: 500,
				changepicturecallback: function () {
					i(), t(".wishlist-select").filter(":visible").change(), t(document).trigger("yith_wcwl_popup_opened", [this])
				},
				markup: '<div class="pp_pic_holder"><div class="ppt"> </div><div class="pp_top"><div class="pp_left"></div><div class="pp_middle"></div><div class="pp_right"></div></div><div class="pp_content_container"><div class="pp_left"><div class="pp_right"><div class="pp_content"><div class="pp_loaderIcon"></div><div class="pp_fade"><a href="#" class="pp_expand" title="Expand the image">Expand</a><div class="pp_hoverContainer"><a class="pp_next" href="#">next</a><a class="pp_previous" href="#">previous</a></div><div id="pp_full_res"></div><div class="pp_details"><a class="pp_close" href="#">Close</a></div></div></div></div></div></div><div class="pp_bottom"><div class="pp_left"></div><div class="pp_middle"></div><div class="pp_right"></div></div></div><div class="pp_overlay yith-wcwl-overlay"></div>'
			};
			t('a[data-rel^="prettyPhoto[add_to_wishlist_"]').add('a[data-rel="prettyPhoto[ask_an_estimate]"]').add('a[data-rel="prettyPhoto[create_wishlist]"]').unbind("click").prettyPhoto(e), t('a[data-rel="prettyPhoto[move_to_another_wishlist]"]').on("click", (function () {
				var i = t(this),
					e = t("#move_to_another_wishlist").find("form"),
					a = e.find(".row-id"),
					n = i.closest("[data-row-id]").data("row-id");
				a.length && a.remove(), e.append('<input type="hidden" name="row_id" class="row-id" value="' + n + '"/>')
			})).prettyPhoto(e);
			var a = function (i, e) {
					if (void 0 !== i.classList && i.classList.contains("yith-wcwl-overlay")) {
						var a = "remove" === e ? "removeClass" : "addClass";
						t("body")[a]("yith-wcwl-with-pretty-photo")
					}
				},
				n = function (t) {
					a(t, "add")
				},
				o = function (t) {
					a(t, "remove")
				};
			new MutationObserver((function (t) {
				for (var i in t) {
					var e = t[i];
					"childList" === e.type && (void 0 !== e.addedNodes && e.addedNodes.forEach(n), void 0 !== e.removedNodes && e.removedNodes.forEach(o))
				}
			})).observe(document.body, {
				childList: !0
			})
		}
	}

	function a() {
		t(".wishlist_table").find('.product-checkbox input[type="checkbox"]').off("change").on("change", (function () {
			var i = t(this);
			i.parent().removeClass("checked").removeClass("unchecked").addClass(i.is(":checked") ? "checked" : "unchecked")
		})).trigger("change")
	}

	function n() {
		t(".add_to_cart").filter("[data-icon]").not(".icon-added").each((function () {
			var i, e = t(this),
				a = e.data("icon");
			i = a.match(/[-a-zA-Z0-9@:%._\+~#=]{1,256}\.[a-zA-Z0-9()]{1,6}\b([-a-zA-Z0-9()@:%_\+.~#?&//=]*)?/gi) ? t("<img/>", {
				src: a
			}) : t("<i/>", {
				class: "fa " + a
			}), e.prepend(i).addClass("icon-added")
		}))
	}

	function o() {
		i(), e(), a(), n(), l(), s(), _(), d(), c(), r(), t(document).trigger("yith_wcwl_init_after_ajax")
	}

	function s() {
		yith_wcwl_l10n.enable_tooltip && t(".yith-wcwl-add-to-wishlist").find("[data-title]").each((function () {
			var i = t(this);
			i.hasClass("tooltip-added") || (i.on("mouseenter", (function () {
				var i, e = t(this),
					a = null,
					n = e.outerWidth(),
					o = 0;
				a = t("<span>", {
					class: "yith-wcwl-tooltip",
					text: e.data("title")
				}), e.append(a), i = a.outerWidth() + 6, a.outerWidth(i), o = (n - i) / 2, a.css({
					left: o.toFixed(0) + "px"
				}).fadeIn(200), e.addClass("with-tooltip")
			})).on("mouseleave", (function () {
				var i = t(this);
				i.find(".yith-wcwl-tooltip").fadeOut(200, (function () {
					i.removeClass("with-tooltip").find(".yith-wcwl-tooltip").remove()
				}))
			})), i.addClass("tooltip-added"))
		}))
	}

	function l() {
		t(".yith-wcwl-add-button").filter(".with-dropdown").on("mouseleave", (function () {
			var i = t(this).find(".yith-wcwl-dropdown");
			i.length && i.fadeOut(200)
		})).children("a").on("mouseenter", (function () {
			var i = t(this).closest(".with-dropdown"),
				e = i.find(".yith-wcwl-dropdown");
			e.length && e.children().length && i.find(".yith-wcwl-dropdown").fadeIn(200)
		}))
	}

	function d() {
		void 0 !== yith_wcwl_l10n.enable_drag_n_drop && yith_wcwl_l10n.enable_drag_n_drop && t(".wishlist_table").filter(".sortable").not(".no-interactions").each((function () {
			var i = t(this),
				e = !1;
			i.sortable({
				items: "[data-row-id]",
				scroll: !0,
				helper: function (i, e) {
					return e.children().each((function () {
						t(this).width(t(this).width())
					})), e
				},
				update: function () {
					var a = i.find("[data-row-id]"),
						n = [],
						o = 0;
					a.length && (e && e.abort(), a.each((function () {
						var i = t(this);
						i.find('input[name*="[position]"]').val(o++), n.push(i.data("row-id"))
					})), e = t.ajax({
						data: {
							action: yith_wcwl_l10n.actions.sort_wishlist_items,
							context: "frontend",
							positions: n,
							wishlist_token: i.data("token"),
							page: i.data("page"),
							per_page: i.data("per-page")
						},
						method: "POST",
						url: yith_wcwl_l10n.ajax_url
					}))
				}
			})
		}))
	}

	function c() {
		var i, e;
		t(".wishlist_table").on("change", ".product-quantity :input", (function () {
			var a = t(this),
				n = a.closest("[data-row-id]"),
				o = n.data("row-id"),
				s = a.closest(".wishlist_table"),
				l = s.data("token");
			clearTimeout(e), n.find(".add_to_cart").attr("data-quantity", a.val()), e = setTimeout((function () {
				i && i.abort(), i = t.ajax({
					beforeSend: function () {
						b(s)
					},
					complete: function () {
						x(s)
					},
					data: {
						action: yith_wcwl_l10n.actions.update_item_quantity,
						context: "frontend",
						product_id: o,
						wishlist_token: l,
						quantity: a.val()
					},
					method: "POST",
					url: yith_wcwl_l10n.ajax_url
				})
			}), 1e3)
		}))
	}

	function r() {
		t(".copy-trigger").on("click", (function () {
			var i = t(".copy-target");
			if (i.length > 0)
				if (i.is("input")) S() ? i[0].setSelectionRange(0, 9999) : i.select(), document.execCommand("copy");
				else {
					var e = t("<input/>", {
						val: i.text(),
						type: "text"
					});
					t("body").append(e), S() ? e[0].setSelectionRange(0, 9999) : e.select(), document.execCommand("copy"), e.remove()
				}
		}))
	}

	function _() {
		t(".wishlist_table").filter(".images_grid").not(".enhanced").on("click", "[data-row-id] .product-thumbnail a", (function (i) {
			var e = t(this).closest("[data-row-id]"),
				a = e.siblings("[data-row-id]"),
				n = e.find(".item-details");
			i.preventDefault(), n.length && (a.removeClass("show"), e.toggleClass("show"))
		})).on("click", "[data-row-id] a.close", (function (i) {
			var e = t(this).closest("[data-row-id]"),
				a = e.find(".item-details");
			i.preventDefault(), a.length && e.removeClass("show")
		})).on("click", "[data-row-id] a.remove_from_wishlist", (function (i) {
			var e = t(this);
			return i.stopPropagation(), w(e), !1
		})).addClass("enhanced"), t(document).on("click", (function (i) {
			t(i.target).closest("[data-row-id]").length || t(".wishlist_table").filter(".images_grid").find(".show").removeClass("show")
		})).on("added_to_cart", (function () {
			t(".wishlist_table").filter(".images_grid").find(".show").removeClass("show")
		}))
	}

	function h(i, e, a) {
		i.action = yith_wcwl_l10n.actions.move_to_another_wishlist_action, i.context = "frontend", "" !== i.wishlist_token && "" !== i.destination_wishlist_token && "" !== i.item_id && t.ajax({
			beforeSend: e,
			url: yith_wcwl_l10n.ajax_url,
			data: i,
			dataType: "json",
			method: "post",
			success: function (e) {
				a(e), o(), t("body").trigger("moved_to_another_wishlist", [t(this), i.item_id])
			}
		})
	}

	function w(i) {
		var e = i.parents(".cart.wishlist_table"),
			a = i.parents("[data-row-id]"),
			n = a.data("row-id"),
			s = e.data("id"),
			l = e.data("token"),
			d = {
				action: yith_wcwl_l10n.actions.remove_from_wishlist_action,
				context: "frontend",
				remove_from_wishlist: n,
				wishlist_id: s,
				wishlist_token: l,
				fragments: j(n)
			};
		t.ajax({
			beforeSend: function () {
				b(e)
			},
			complete: function () {
				x(e)
			},
			data: d,
			method: "post",
			success: function (e) {
				void 0 !== e.fragments && T(e.fragments), o(), t("body").trigger("removed_from_wishlist", [i, a])
			},
			url: yith_wcwl_l10n.ajax_url
		})
	}

	function f(i) {
		var e = t(this),
			a = e.closest(".wishlist_table"),
			n = null;
		i.preventDefault(), (n = a.length ? e.closest("[data-wishlist-id]").find(".wishlist-title") : e.parents(".wishlist-title")).next().css("display", "inline-block").find('input[type="text"]').focus(), n.hide()
	}

	function p(i) {
		var e = t(this);
		i.preventDefault(), e.parents(".hidden-title-form").hide(), e.parents(".hidden-title-form").prev().show()
	}

	function u(i) {
		var e, a = t(this),
			n = a.closest(".hidden-title-form"),
			o = a.closest("[data-wishlist-id]").data("wishlist-id"),
			s = n.find('input[type="text"]'),
			l = s.val();
		if (i.preventDefault(), !l) return n.addClass("woocommerce-invalid"), void s.focus();
		o || (o = t("#wishlist_id").val()), e = {
			action: yith_wcwl_l10n.actions.save_title_action,
			context: "frontend",
			wishlist_id: o,
			title: l,
			fragments: j()
		}, t.ajax({
			type: "POST",
			url: yith_wcwl_l10n.ajax_url,
			data: e,
			dataType: "json",
			beforeSend: function () {
				b(n)
			},
			complete: function () {
				x(n)
			},
			success: function (t) {
				var i = t.fragments;
				t.result ? (n.hide(), n.prev().find(".wishlist-anchor, h1, h2").text(l).end().show()) : (n.addClass("woocommerce-invalid"), s.focus()), void 0 !== i && T(i)
			}
		})
	}

	function m() {
		var i = t(this),
			e = i.val(),
			a = i.closest("[data-wishlist-id]").data("wishlist-id"),
			n = {
				action: yith_wcwl_l10n.actions.save_privacy_action,
				context: "frontend",
				wishlist_id: a,
				privacy: e,
				fragments: j()
			};
		t.ajax({
			type: "POST",
			url: yith_wcwl_l10n.ajax_url,
			data: n,
			dataType: "json",
			success: function (t) {
				var i = t.fragments;
				void 0 !== i && T(i)
			}
		})
	}

	function v(i) {
		if (void 0 !== t.prettyPhoto && void 0 !== t.prettyPhoto.close)
			if (void 0 !== i) {
				var e = t(".pp_content_container"),
					a = e.find(".pp_content"),
					n = e.find(".yith-wcwl-popup-form"),
					o = n.closest(".pp_pic_holder");
				if (n.length) {
					var s = t("<div/>", {
						class: "yith-wcwl-popup-feedback"
					});
					s.append(t("<i/>", {
						class: "fa fa-check heading-icon"
					})), s.append(t("<p/>", {
						class: "feedback",
						html: i
					})), s.css("display", "none"), a.css("height", "auto"), n.after(s), n.fadeOut(200, (function () {
						s.fadeIn()
					})), o.addClass("feedback"), o.css("left", t(window).innerWidth() / 2 - o.outerWidth() / 2 + "px"), (void 0 === yith_wcwl_l10n.auto_close_popup || yith_wcwl_l10n.auto_close_popup) && setTimeout(v, yith_wcwl_l10n.popup_timeout)
				}
			} else try {
				t.prettyPhoto.close()
			} catch (t) {}
	}

	function g(i) {
		var e = t("#yith-wcwl-popup-message"),
			a = t("#yith-wcwl-message"),
			n = void 0 !== yith_wcwl_l10n.popup_timeout ? yith_wcwl_l10n.popup_timeout : 3e3;
		(void 0 === yith_wcwl_l10n.enable_notices || yith_wcwl_l10n.enable_notices) && (a.html(i), e.css("margin-left", "-" + t(e).width() + "px").fadeIn(), window.setTimeout((function () {
			e.fadeOut()
		}), n))
	}

	function y(i) {
		var e = t("select.wishlist-select"),
			a = t("ul.yith-wcwl-dropdown");
		e.each((function () {
			var e = t(this),
				a = e.find("option"),
				n = a.filter('[value="new"]');
			a.not(n).remove(), t.each(i, (function (i, a) {
				t("<option>", {
					value: a.id,
					html: a.wishlist_name
				}).appendTo(e)
			})), e.append(n)
		})), a.each((function () {
			var e = t(this),
				a = e.find("li"),
				n = e.closest(".yith-wcwl-add-button").children("a.add_to_wishlist"),
				o = n.attr("data-product-id"),
				s = n.attr("data-product-type");
			a.remove(), t.each(i, (function (i, a) {
				a.default || t("<li>").append(t("<a>", {
					rel: "nofollow",
					html: a.wishlist_name,
					class: "add_to_wishlist",
					href: a.add_to_this_wishlist_url,
					"data-product-id": o,
					"data-product-type": s,
					"data-wishlist-id": a.id
				})).appendTo(e)
			}))
		}))
	}

	function b(i) {
		void 0 !== t.fn.block && i.fadeTo("400", "0.6").block({
			message: null,
			overlayCSS: {
				background: "transparent url(" + yith_wcwl_l10n.ajax_loader_url + ") no-repeat center",
				backgroundSize: "40px 40px",
				opacity: 1
			}
		})
	}

	function x(i) {
		void 0 !== t.fn.unblock && i.stop(!0).css("opacity", "1").unblock()
	}

	function k() {
		if (navigator.cookieEnabled) return !0;
		document.cookie = "cookietest=1";
		var t = -1 !== document.cookie.indexOf("cookietest=");
		return document.cookie = "cookietest=1; expires=Thu, 01-Jan-1970 00:00:01 GMT", t
	}

	function j(i) {
		var e = {},
			a = null;
		return i ? "object" == typeof i ? (a = (i = t.extend({
			fragments: null,
			s: "",
			container: t(document),
			firstLoad: !1
		}, i)).fragments ? i.fragments : i.container.find(".wishlist-fragment"), i.s && (a = a.not("[data-fragment-ref]").add(a.filter('[data-fragment-ref="' + i.s + '"]'))), i.firstLoad && (a = a.filter(".on-first-load"))) : (a = t(".wishlist-fragment"), "string" != typeof i && "number" != typeof i || (a = a.not("[data-fragment-ref]").add(a.filter('[data-fragment-ref="' + i + '"]')))) : a = t(".wishlist-fragment"), a.length ? (a.each((function () {
			var i = t(this),
				a = i.attr("class").split(" ").filter(t => t.length && "exists" !== t).join(yith_wcwl_l10n.fragments_index_glue);
			e[a] = i.data("fragment-options")
		})), e) : null
	}

	function C(i) {
		var e = j(i = t.extend({
			firstLoad: !0
		}, i));
		e && t.ajax({
			data: {
				action: yith_wcwl_l10n.actions.load_fragments,
				context: "frontend",
				fragments: e
			},
			method: "post",
			success: function (a) {
				void 0 !== a.fragments && (T(a.fragments), o(), t(document).trigger("yith_wcwl_fragments_loaded", [e, a.fragments, i.firstLoad]))
			},
			url: yith_wcwl_l10n.ajax_url
		})
	}

	function T(i) {
		t.each(i, (function (i, e) {
			var a = "." + i.split(yith_wcwl_l10n.fragments_index_glue).filter(t => t.length && "exists" !== t).join("."),
				n = t(a),
				o = t(e).filter(a);
			o.length || (o = t(e).find(a)), n.length && o.length && n.replaceWith(o)
		}))
	}

	function S() {
		return navigator.userAgent.match(/ipad|iphone/i)
	}

	function P(t) {
		return !0 === t || "yes" === t || "1" === t || 1 === t
	}
	t(document).on("yith_wcwl_init", (function () {
		var S = t(this),
			O = "undefined" != typeof wc_add_to_cart_params && null !== wc_add_to_cart_params ? wc_add_to_cart_params.cart_redirect_after_add : "";
		S.on("click", ".add_to_wishlist", (function (i) {
				var e, a = t(this),
					n = a.attr("data-product-id"),
					s = t(".add-to-wishlist-" + n),
					l = {
						action: yith_wcwl_l10n.actions.add_to_wishlist_action,
						context: "frontend",
						add_to_wishlist: n,
						product_type: a.data("product-type"),
						wishlist_id: a.data("wishlist-id"),
						fragments: j(n)
					};
				if ((e = t(document).triggerHandler("yith_wcwl_add_to_wishlist_data", [a, l])) && (l = e), i.preventDefault(), jQuery(document.body).trigger("adding_to_wishlist"), yith_wcwl_l10n.multi_wishlist && yith_wcwl_l10n.modal_enable) {
					var d = a.parents(".yith-wcwl-popup-footer").prev(".yith-wcwl-popup-content"),
						c = d.find(".wishlist-select"),
						r = d.find(".wishlist-name"),
						_ = d.find(".wishlist-visibility").filter(":checked");
					if (l.wishlist_id = c.is(":visible") ? c.val() : "new", l.wishlist_name = r.val(), l.wishlist_visibility = _.val(), "new" === l.wishlist_id && !l.wishlist_name) return r.closest("p").addClass("woocommerce-invalid"), !1;
					r.closest("p").removeClass("woocommerce-invalid")
				}
				if (k()) return t.ajax({
					type: "POST",
					url: yith_wcwl_l10n.ajax_url,
					data: l,
					dataType: "json",
					beforeSend: function () {
						b(a)
					},
					complete: function () {
						x(a)
					},
					success: function (i) {
						var e = i.result,
							n = i.message;
						yith_wcwl_l10n.multi_wishlist ? (v(n), void 0 !== i.user_wishlists && y(i.user_wishlists)) : g(n), "true" !== e && "exists" !== e || (void 0 !== i.fragments && T(i.fragments), yith_wcwl_l10n.multi_wishlist && !yith_wcwl_l10n.hide_add_button || s.find(".yith-wcwl-add-button").remove(), s.addClass("exists")), o(), t("body").trigger("added_to_wishlist", [a, s])
					}
				}), !1;
				window.alert(yith_wcwl_l10n.labels.cookie_disabled)
			})), S.on("click", ".wishlist_table .remove_from_wishlist", (function (i) {
				var e = t(this);
				return i.preventDefault(), w(e), !1
			})), S.on("adding_to_cart", "body", (function (t, i, e) {
				void 0 !== i && void 0 !== e && i.closest(".wishlist_table").length && (e.remove_from_wishlist_after_add_to_cart = i.closest("[data-row-id]").data("row-id"), e.wishlist_id = i.closest(".wishlist_table").data("id"), "undefined" != typeof wc_add_to_cart_params && (wc_add_to_cart_params.cart_redirect_after_add = yith_wcwl_l10n.redirect_to_cart), "undefined" != typeof yith_wccl_general && (yith_wccl_general.cart_redirect = P(yith_wcwl_l10n.redirect_to_cart)))
			})), S.on("added_to_cart", "body", (function (t, i, e, a) {
				if (void 0 !== a && a.closest(".wishlist_table").length) {
					"undefined" != typeof wc_add_to_cart_params && (wc_add_to_cart_params.cart_redirect_after_add = O), "undefined" != typeof yith_wccl_general && (yith_wccl_general.cart_redirect = P(O));
					var n = a.closest("[data-row-id]"),
						o = n.closest(".wishlist-fragment").data("fragment-options");
					a.removeClass("added"), n.find(".added_to_cart").remove(), yith_wcwl_l10n.remove_from_wishlist_after_add_to_cart && o.is_user_owner && n.remove()
				}
			})), S.on("added_to_cart", "body", (function () {
				var i = t(".woocommerce-message");
				0 === i.length ? t("#yith-wcwl-form").prepend(yith_wcwl_l10n.labels.added_to_cart_message) : i.fadeOut(300, (function () {
					t(this).replaceWith(yith_wcwl_l10n.labels.added_to_cart_message).fadeIn()
				}))
			})), S.on("cart_page_refreshed", "body", o), S.on("click", ".show-title-form", f), S.on("click", ".wishlist-title-with-form h2", f), S.on("click", ".remove_from_all_wishlists", (function (i) {
				var e = t(this),
					a = e.attr("data-product-id"),
					n = e.data("wishlist-id"),
					s = e.closest(".content"),
					l = {
						action: yith_wcwl_l10n.actions.remove_from_all_wishlists,
						context: "frontend",
						prod_id: a,
						wishlist_id: n,
						fragments: j(a)
					};
				i.preventDefault(), t.ajax({
					beforeSend: function () {
						b(s)
					},
					complete: function () {
						x(s)
					},
					data: l,
					dataType: "json",
					method: "post",
					success: function (t) {
						void 0 !== t.fragments && T(t.fragments), o()
					},
					url: yith_wcwl_l10n.ajax_url
				})
			})), S.on("click", ".hide-title-form", p), S.on("click", ".save-title-form", u), S.on("change", ".wishlist_manage_table .wishlist-visibility", m), S.on("change", ".change-wishlist", (function () {
				var i = t(this),
					e = i.parents(".cart.wishlist_table"),
					a = e.data("token"),
					n = i.parents("[data-row-id]").data("row-id");
				h({
					wishlist_token: a,
					destination_wishlist_token: i.val(),
					item_id: n,
					fragments: j()
				}, (function () {
					b(e)
				}), (function (t) {
					void 0 !== t.fragments && T(t.fragments), x(e)
				}))
			})), S.on("click", ".yith-wcwl-popup-footer .move_to_wishlist", (function () {
				var i = t(this),
					e = i.attr("data-product-id"),
					a = i.data("origin-wishlist-id"),
					n = i.closest("form"),
					s = n.find(".wishlist-select").val(),
					l = n.find(".wishlist-name"),
					d = l.val(),
					c = n.find(".wishlist-visibility").filter(":checked").val();
				if ("new" === s && !d) return l.closest("p").addClass("woocommerce-invalid"), !1;
				l.closest("p").removeClass("woocommerce-invalid"), h({
					wishlist_token: a,
					destination_wishlist_token: s,
					item_id: e,
					wishlist_name: d,
					wishlist_visibility: c,
					fragments: j(e)
				}, (function () {
					b(i)
				}), (function (t) {
					var e = t.message;
					yith_wcwl_l10n.multi_wishlist ? (v(e), void 0 !== t.user_wishlists && y(t.user_wishlists)) : g(e), void 0 !== t.fragments && T(t.fragments), o(), x(i)
				}))
			})), S.on("click", ".delete_item", (function () {
				var i = t(this),
					e = i.attr("data-product-id"),
					a = i.data("item-id"),
					n = t(".add-to-wishlist-" + e),
					s = {
						action: yith_wcwl_l10n.actions.delete_item_action,
						context: "frontend",
						item_id: a,
						fragments: j(e)
					};
				return t.ajax({
					url: yith_wcwl_l10n.ajax_url,
					data: s,
					dataType: "json",
					beforeSend: function () {
						b(i)
					},
					complete: function () {
						x(i)
					},
					method: "post",
					success: function (e) {
						var a = e.fragments,
							s = e.message;
						yith_wcwl_l10n.multi_wishlist && v(s), i.closest(".yith-wcwl-remove-button").length || g(s), void 0 !== a && T(a), o(), t("body").trigger("removed_from_wishlist", [i, n])
					}
				}), !1
			})), S.on("change", ".yith-wcwl-popup-content .wishlist-select", (function () {
				var i = t(this);
				"new" === i.val() ? i.parents(".yith-wcwl-first-row").next(".yith-wcwl-second-row").show() : i.parents(".yith-wcwl-first-row").next(".yith-wcwl-second-row").hide()
			})), S.on("change", "#bulk_add_to_cart", (function () {
				var i = t(this),
					e = i.closest(".wishlist_table").find("[data-row-id]").find('input[type="checkbox"]:not(:disabled)');
				i.is(":checked") ? e.prop("checked", "checked").change() : e.removeProp("checked").change()
			})), S.on("submit", ".wishlist-ask-an-estimate-popup", (function () {
				var i = t(this),
					e = i.closest("form"),
					a = i.closest(".pp_content"),
					n = e.serializeArray().reduce((t, i) => (t[i.name] = i.value, t), {});
				return n.action = yith_wcwl_l10n.actions.ask_an_estimate, n.context = "frontend", t.ajax({
					beforeSend: function () {
						b(e)
					},
					complete: function () {
						x(e)
					},
					data: n,
					dataType: "json",
					method: "post",
					success: function (i) {
						if (void 0 !== i.result && i.result) {
							var n = i.template;
							void 0 !== n && (e.replaceWith(n), a.css("height", "auto"), setTimeout(v, yith_wcwl_l10n.time_to_close_prettyphoto))
						} else void 0 !== i.message && (e.find(".woocommerce-error").remove(), e.find(".popup-description").after(t("<div>", {
							text: i.message,
							class: "woocommerce-error"
						})))
					},
					url: yith_wcwl_l10n.ajax_url
				}), !1
			})), S.on("click", ".yith-wfbt-add-wishlist", (function (i) {
				i.preventDefault();
				var e = t(this),
					a = t("#yith-wcwl-form");
				t("html, body").animate({
						scrollTop: a.offset().top
					}, 500),
					function (i, e) {
						var a = i.attr("data-product-id"),
							n = t(document).find(".cart.wishlist_table"),
							s = n.data("pagination"),
							l = n.data("per-page"),
							d = n.data("id"),
							c = n.data("token"),
							r = {
								action: yith_wcwl_l10n.actions.reload_wishlist_and_adding_elem_action,
								context: "frontend",
								pagination: s,
								per_page: l,
								wishlist_id: d,
								wishlist_token: c,
								add_to_wishlist: a,
								product_type: i.data("product-type")
							};
						if (!k()) return void window.alert(yith_wcwl_l10n.labels.cookie_disabled);
						t.ajax({
							type: "POST",
							url: yith_wcwl_l10n.ajax_url,
							data: r,
							dataType: "html",
							beforeSend: function () {
								b(n)
							},
							complete: function () {
								x(n)
							},
							success: function (i) {
								var a = t(i),
									n = a.find("#yith-wcwl-form"),
									s = a.find(".yith-wfbt-slider-wrapper");
								e.replaceWith(n), t(".yith-wfbt-slider-wrapper").replaceWith(s), o(), t(document).trigger("yith_wcwl_reload_wishlist_from_frequently")
							}
						})
					}(e, a)
			})), S.on("submit", ".yith-wcwl-popup-form", (function () {
				return !1
			})), S.on("yith_infs_added_elem", (function () {
				e()
			})), S.on("found_variation", (function (i, e) {
				var a = t(i.target).data("product_id"),
					n = e.variation_id,
					o = t('[data-product-id="' + a + '"]').add('[data-original-product-id="' + a + '"]'),
					s = o.closest(".wishlist-fragment").filter(":visible");
				a && n && o.length && (o.each((function () {
					var i, e = t(this),
						o = e.closest(".yith-wcwl-add-to-wishlist");
					e.attr("data-original-product-id", a), e.attr("data-product-id", n), o.length && (void 0 !== (i = o.data("fragment-options")) && (i.product_id = n, o.data("fragment-options", i)), o.removeClass((function (t, i) {
						return i.match(/add-to-wishlist-\S+/g).join(" ")
					})).addClass("add-to-wishlist-" + n).attr("data-fragment-ref", n))
				})), yith_wcwl_l10n.reload_on_found_variation && (b(s), C({
					fragments: s,
					firstLoad: !1
				})))
			})), S.on("reset_data", (function (i) {
				var e = t(i.target).data("product_id"),
					a = t('[data-original-product-id="' + e + '"]'),
					n = a.closest(".wishlist-fragment").filter(":visible");
				e && a.length && (a.each((function () {
					var i, a = t(this),
						n = a.closest(".yith-wcwl-add-to-wishlist"),
						o = a.attr("data-product-id");
					a.attr("data-product-id", e), a.attr("data-original-product-id", ""), n.length && (void 0 !== (i = n.data("fragment-options")) && (i.product_id = e, n.data("fragment-options", i)), n.removeClass("add-to-wishlist-" + o).addClass("add-to-wishlist-" + e).attr("data-fragment-ref", e))
				})), yith_wcwl_l10n.reload_on_found_variation && (b(n), C({
					fragments: n,
					firstLoad: !1
				})))
			})), S.on("yith_wcwl_reload_fragments", C), S.on("yith_infs_added_elem", (function (t, i) {
				C({
					container: i,
					firstLoad: !1
				})
			})), S.on("yith_wcwl_fragments_loaded", (function (i, e, a, n) {
				n && t(".variations_form").find(".variations select").last().change()
			})), S.on("click", ".yith-wcwl-popup-feedback .close-popup", (function (t) {
				t.preventDefault(), v()
			})),
			function () {
				if (void 0 !== yith_wcwl_l10n.enable_notices && !yith_wcwl_l10n.enable_notices) return;
				if (t(".yith-wcwl-add-to-wishlist").length && !t("#yith-wcwl-popup-message").length) {
					var i = t("<div>").attr("id", "yith-wcwl-message"),
						e = t("<div>").attr("id", "yith-wcwl-popup-message").html(i).hide();
					t("body").prepend(e)
				}
			}(), s(), l(), d(), c(), _(), t(document).on("click", ".show-tab", (function (i) {
				var e = t(this),
					a = e.closest(".yith-wcwl-popup-content"),
					n = e.data("tab"),
					o = a.find(".tab").filter("." + n);
				if (i.preventDefault(), !o.length) return !1;
				e.addClass("active").siblings(".show-tab").removeClass("active"), o.show().siblings(".tab").hide(), "create" === n ? a.prepend('<input type="hidden" id="new_wishlist_selector" class="wishlist-select" value="new">') : a.find("#new_wishlist_selector").remove()
			})), t(document).on("change", ".wishlist-select", (function () {
				var i = t(this),
					e = i.closest(".yith-wcwl-popup-content"),
					a = i.closest(".tab"),
					n = e.find(".tab.create"),
					o = e.find(".show-tab"),
					s = o.filter('[data-tab="create"]');
				"new" === i.val() && n.length && (a.hide(), n.show(), o.removeClass("active"), s.addClass("active"), i.find("option").removeProp("selected"), i.change())
			})), i(), a(), e(), n(),
			function () {
				var i = !1;
				if (!yith_wcwl_l10n.is_wishlist_responsive) return;
				t(window).on("resize", (function () {
					var e = t(".wishlist_table.responsive"),
						a = e.is(".mobile"),
						n = window.matchMedia("(max-width: 768px)"),
						s = e.closest("form"),
						l = s.attr("class"),
						d = s.data("fragment-options"),
						c = {},
						r = !1;
					e.length && (n.matches && e && !a ? (d.is_mobile = "yes", r = !0) : !n.matches && e && a && (d.is_mobile = "no", r = !0), r && (i && i.abort(), c[l.split(" ").join(yith_wcwl_l10n.fragments_index_glue)] = d, i = t.ajax({
						beforeSend: function () {
							b(e)
						},
						complete: function () {
							x(e)
						},
						data: {
							action: yith_wcwl_l10n.actions.load_mobile_action,
							context: "frontend",
							fragments: c
						},
						method: "post",
						success: function (i) {
							void 0 !== i.fragments && (T(i.fragments), o(), t(document).trigger("yith_wcwl_responsive_template", [a, i.fragments]))
						},
						url: yith_wcwl_l10n.ajax_url
					})))
				}))
			}(), r(), yith_wcwl_l10n.enable_ajax_loading && C()
	})).trigger("yith_wcwl_init")
}));