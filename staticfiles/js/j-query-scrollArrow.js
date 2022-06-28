//スクロールした際の動きを関数でまとめる
function PageTopCheck() {
	var winScrollTop = $(this).scrollTop();
	// var secondTop =  $("contact").offset().top - 150 → #contactの上から150pxの位置まで来たら
	// 全ページで矢印が切り替わるように、#changedArrowでコントロールしている
	var secondTop = $("#changedArrow").offset().top - 300; // #changedArrowの上から300pxで変化する
	if (winScrollTop >= secondTop) {
		$('.js-scroll').removeClass('scroll-view');//.js-scrollからscroll-viewというクラス名を除去
		$('.js-pagetop').addClass('scroll-view');//.js-pagetopにscroll-viewというクラス名を付与
	} else {//元に戻ったら
		$('.js-scroll').addClass('scroll-view');//.js-scrollからscroll-viewというクラス名を付与
		$('.js-pagetop').removeClass('scroll-view');//.js-pagetopからscroll-viewというクラス名を除去
	}

}

//クリックした際の動き
$('.scroll-top a').click(function () {
	var elmHash = $(this).attr('href'); //hrefの内容を取得
	if (elmHash == "#changedArrow") {//もし、リンク先のhrefの後が#changedArrowの場合
		var pos = $(elmHash).offset().top;
		$('body,html').animate({ scrollTop: pos }, pos); //#contactにスクロール
	} else {
		$('body,html').animate({ scrollTop: 0 }, 500); //それ以外はトップへスクロール。数字が大きくなるほどゆっくりスクロール
	}
	return false;//リンク自体の無効化
});

// 画面をスクロールをしたら動かしたい場合の記述
$(window).scroll(function () {
	PageTopCheck();/* スクロールした際の動きの関数を呼ぶ*/
});

// ページが読み込まれたらすぐに動かしたい場合の記述
$(window).on('load', function () {
	PageTopCheck();/* スクロールした際の動きの関数を呼ぶ*/
});