/* JS Document */

/******************************

[Table of Contents]

1. Vars and Inits
2. Set Header
3. Init Menu
4. Init Input
5. Init Google Map


******************************/

$(document).ready(function()
{
	"use strict";

	/* 

	1. Vars and Inits

	*/

	var header = $('.header');
	var headerSocial = $('.header_social');
	var menu = $('.menu');
	var menuActive = false;
	var burger = $('.hamburger');
	var map;

	setHeader();

	$(window).on('resize', function()
	{
		setHeader();

		setTimeout(function()
		{
			$(window).trigger('resize.px.parallax');
		}, 375);
	});

	$(document).on('scroll', function()
	{
		setHeader();
	});

	initMenu();
	initInput();
	

	/* 

	2. Set Header

	*/

	function setHeader()
	{
		if($(window).scrollTop() > 127)
		{
			header.addClass('scrolled');
			headerSocial.addClass('scrolled');
		}
		else
		{
			header.removeClass('scrolled');
			headerSocial.removeClass('scrolled');
		}
	}

	/* 

	3. Set Menu

	*/

	function initMenu()
	{
		if($('.menu').length)
		{
			var menu = $('.menu');
			if($('.hamburger').length)
			{
				burger.on('click', function()
				{
					if(menuActive)
					{
						closeMenu();
					}
					else
					{
						openMenu();
					}
				});
			}
		}
		if($('.menu_close').length)
		{
			var close = $('.menu_close');
			close.on('click', function()
			{
				if(menuActive)
				{
					closeMenu();
				}
			});
		}
	}

	function openMenu()
	{
		menu.addClass('active');
		menuActive = true;
	}

	function closeMenu()
	{
		menu.removeClass('active');
		menuActive = false;
	}

	/* 

	4. Init Input

	*/

	function initInput()
	{
		if($('.inpt').length)
		{
			var inpt = $('.inpt');
			inpt.each(function()
			{
				var ele = $(this);
				var border = ele.next();

				ele.focus(function()
				{
					border.css({'visibility': "visible", 'opacity': "1"});
				});
				ele.blur(function()
				{
					border.css({'visibility': "hidden", 'opacity': "0"});
				});

				ele.on("mouseenter", function()
				{
					border.css({'visibility': "visible", 'opacity': "1"});
				});

				ele.on("mouseleave", function()
				{
					if(!ele.is(":focus"))
					{
						border.css({'visibility': "hidden", 'opacity': "0"});
					}
				});
				
			});
		}
	}

	 /* 

	5. Init Google Map

	*/

	
	
});


/* JS for the cart */



$(document).ready(function() {
 
	/* Set rates + misc */
	var taxRate = 0.05;
	var shippingRate = 15.00; 
	var fadeTime = 300;
	 
	 
	/* Assign actions */
	$('.product-quantity input').change( function() {
	  updateQuantity(this);
	});
	 
	$('.product-removal button').click( function() {
	  removeItem(this);
	});
	 
	 
	/* Recalculate cart */
	function recalculateCart()
	{
	  var subtotal = 0;
	   
	  /* Sum up row totals */
	  $('.product').each(function () {
		subtotal += parseFloat($(this).children('.product-line-price').text());
	  });
	   
	  /* Calculate totals */
	  var tax = subtotal * taxRate;
	  var shipping = (subtotal > 0 ? shippingRate : 0);
	  var total = subtotal + tax + shipping;
	   
	  /* Update totals display */
	  $('.totals-value').fadeOut(fadeTime, function() {
		$('#cart-subtotal').html(subtotal.toFixed(2));
		$('#cart-tax').html(tax.toFixed(2));
		$('#cart-shipping').html(shipping.toFixed(2));
		$('#cart-total').html(total.toFixed(2));
		if(total == 0){
		  $('.checkout').fadeOut(fadeTime);
		}else{
		  $('.checkout').fadeIn(fadeTime);
		}
		$('.totals-value').fadeIn(fadeTime);
	  });
	}
	 
	 
	/* Update quantity */
	function updateQuantity(quantityInput)
	{
	  /* Calculate line price */
	  var productRow = $(quantityInput).parent().parent();
	  var price = parseFloat(productRow.children('.product-price').text());
	  var quantity = $(quantityInput).val();
	  var linePrice = price * quantity;
	   
	  /* Update line price display and recalc cart totals */
	  productRow.children('.product-line-price').each(function () {
		$(this).fadeOut(fadeTime, function() {
		  $(this).text(linePrice.toFixed(2));
		  recalculateCart();
		  $(this).fadeIn(fadeTime);
		});
	  });  
	}
	 
	 
	/* Remove item from cart */
	function removeItem(removeButton)
	{
	  /* Remove row from DOM and recalc cart total */
	  var productRow = $(removeButton).parent().parent();
	  productRow.slideUp(fadeTime, function() {
		productRow.remove();
		recalculateCart();
	  });
	}
	 
	});