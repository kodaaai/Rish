// $(function() {
//     var words = [
//           "ActionScript",
//           "AppleScript",
//           "Asp",
//           "BASIC",
//           "C",
//           "C++",
//           "Clojure",
//           "COBOL",
//           "ColdFusion",
//           "Erlang",
//           "Fortran",
//           "Groovy",
//           "Haskell",
//           "Java",
//           "JavaScript",
//           "Lisp",
//           "Perl",
//           "PHP",
//           "Python",
//           "Ruby",
//           "Scala",
//           "Scheme",
//         ];
//         $( "#keyword" ).autocomplete({
//           source: words,
//         });
//     });
$(function () {
  var words = [
    { label: "財政学", kana: "ざいせいがく" },
    { label: "マクロ経済学（基礎）", kana: "まくろけいざいがくきそ" },
    { label: "マクロ経済学（応用）", kana: "まくろけいざいがくおうよう" },
    { label: "宮田亮", kana: "みやたりょう" }
  ];
  $("#keyword").autocomplete({
    source: function (request, response) {
      var list = [];
      list = words.filter(function (word) {
        return (
          word.label.indexOf(request.term) === 0 ||
          word.kana.indexOf(request.term) === 0
        );
      });
      response(list);
    }
  });
});


/* レビュー投稿画面におけるサジェスチョン */

const suggestions = ["subject_class", "scoring_method",]
/* サジェストを反映させる処理 */
$(document).ready(function () {
  suggestions.forEach((suggestion) => {
    $(`#id_${suggestion}`).select2({
      theme: "bootstrap-5",
      width: $(this).data('width') ? $(this).data('width') : $(this).hasClass('w-100') ? '100%' : 'style',
      placeholder: '選択肢の中から選んでください。',
      closeOnSelect: false,

      /* 検索結果が見つからなかった場合の選択肢の設定 */
      "language": {
        "noResults": function () {
          return '検索結果がありません。';
        }
      },
      escapeMarkup: function (markup) {
        return markup;
      }
    });
  })
});


/* 新規追加可能な項目 */
const suggestions_add = ["class_name", "teacher", "tag",]
$(document).ready(function () {
  suggestions_add.forEach((suggestion) => {
    $(`#id_${suggestion}`).select2({

      /* bootstrapのスタイル適用 */
      theme: "bootstrap-5",
      width: $(this).data('width') ? $(this).data('width') : $(this).hasClass('w-100') ? '100%' : 'style',
      placeholder: '選択肢の中から選んでください。',
      closeOnSelect: false,

      /* 検索結果が見つからなかった場合の選択肢の設定 */
      "language": {
        "noResults": function () {
          return `<a href='./review/${suggestion}_create' class='btn btn-outline-secondary'>登録されていないようです。こちらから新規追加をすることができます。</a>`;
        }
      },
      escapeMarkup: function (markup) {
        return markup;
      },
    });
  })
});

/* -------------suggestionここまで-------------- */



