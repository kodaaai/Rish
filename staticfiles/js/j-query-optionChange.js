
/* 学部の入力に応じて学科の表示を変える */
const subject = {

    人文社会学部: [
        '国際法政学科',
        '人間社会学科',
        '琉球アジア文化学科',
    ],

    国際地域創造学部: [
        '国際地域創造学科'
    ],

    教育学部: [
        '学校教育教員養成課程'
    ],

    理学部: [
        '数理科学科',
        '物質地球科学科',
        '海洋自然科学科',
    ],

    医学部: [
        '医学科',
        '保健学科',
    ],

    工学部: [
        '工学科',
    ],

    農学部: [
        '亜熱帯地域農学科',
        '亜熱帯農林環境科学科',
        '地域農業工学科',
        '亜熱帯生物資源科学科',
    ]

}

$(document).ready(function () {
    $('#id_department').on('change', function () {

        let departVal = $(this).val(); //選択された項目のvalueを取得

        if (departVal) { //valueに何か値が入っていた場合

            const item = subject[departVal];

            $('#id_subject').html('');
            $('#id_course').html('');
            $('#id_course').append('<option value="" >選択してください（任意）</option>')
            $('#id_major').html('');
            $('#id_major').append('<option value="" >選択してください（任意）</option>')
            $('#id_specialization').html('');
            $('#id_specialization').append('<option value="" >選択してください（任意）</option>')

            let option;

            $('#id_subject').append('<option value="" >選択してください（必須）</option>')
            for (let i = 0; i < item.length; i++) {

                option = '<option value="' + item[i] + '">' + item[i] + '</option>';

                $('#id_subject').append(option);

            }

        } else { //valueに何も値が入っていない場合
            $('#id_subject').html('');
            $('#id_subject').append('<option value="" >選択してください（任意）</option>')
            $('#id_course').html('');
            $('#id_course').append('<option value="" >選択してください（任意）</option>')
            $('#id_major').html('');
            $('#id_major').append('<option value="" >選択してください（任意）</option>')
            $('#id_specialization').html('');
            $('#id_specialization').append('<option value="" >選択してください（任意）</option>')
        }
    })
});




/* 学科の入力に応じてコース・プログラムの表示を変える */
const course = {
    /* 人文社会学部 */
    国際法政学科: [
        '法学プログラム',
        '政治・国際関係学プログラム',
    ],

    人間社会学科: [
        '哲学・教育学プログラム',
        '心理学プログラム',
        '社会学プログラム',
    ],

    琉球アジア文化学科: [
        '歴史・民俗学プログラム',
        '言語学プログラム',
        '文学プログラム',
    ],

    国際地域創造学科: [
        '観光地域デザインプログラム',
        '経済学プログラム',
        '地域文化科学プログラム',
        '国際言語文化プログラム',
        '経営プログラム',
    ],

    学校教育教員養成課程: [
        '小学校教育コース',
        '中学校教育コース',
        '特別支援教育コース',
    ],

    物質地球科学科: [
        '物理系',
        '地学系',
    ],

    海洋自然科学科: [
        '化学系',
        '生物系'
    ],

    工学科: [
        '機械工学コース',
        'エネルギー環境工学コース',
        '電気システム工学コース',
        '社会基盤デザインコース',
        '建築学コース',
        '知能情報コース',
    ],

    亜熱帯生物資源科学科: [
        '健康栄養科学コース',
    ]

}

$(document).ready(function () {
    $('#id_subject').on('change', function () {

        let subjectVal = $(this).val(); //選択された項目のvalueを取得

        if (subjectVal) { //valueに何か値が入っていた場合

            const item = course[subjectVal];

            $('#id_course').html('');
            $('#id_major').html('');
            $('#id_major').append('<option value="" >選択してください（任意）</option>')
            $('#id_specialization').html('');
            $('#id_specialization').append('<option value="" >選択してください（任意）</option>')
            let option;

            $('#id_course').append('<option value="" >選択してください（任意）</option>')
            for (let i = 0; i < item.length; i++) {

                option = '<option value="' + item[i] + '">' + item[i] + '</option>';

                $('#id_course').append(option);

            }

        } else { //valueに何も値が入っていない場合

            $('#id_course').html('');
            $('#id_course').append('<option value="" >選択してください（任意）</option>')
            $('#id_major').html('');
            $('#id_major').append('<option value="" >選択してください（任意）</option>')
            $('#id_specialization').html('');
            $('#id_specialization').append('<option value="" >選択してください（任意）</option>') //保存された最初の状態に戻す

        }
    })
});



/* コース・プログラムに応じて、専攻の表示を変える */

const major = {

    小学校教育コース: [
        '学校教育専攻',
        '教科教育専攻',
    ],

    中学校教育コース: [
        '教科教育専攻',
    ],

    特別支援教育コース: [
        '特別支援教育専攻',
    ],

}

$(document).ready(function () {
    $('#id_course').on('change', function () {

        let courseVal = $(this).val(); //選択された項目のvalueを取得

        if (courseVal) { //valueに何か値が入っていた場合

            const item = major[courseVal];

            $('#id_major').html('');
            $('#id_specialization').html('');
            $('#id_specialization').append('<option value="" >選択してください（任意）</option>')

            let option;

            $('#id_major').append('<option value="" >選択してください（任意）</option>')
            for (let i = 0; i < item.length; i++) {

                option = '<option value="' + item[i] + '">' + item[i] + '</option>';

                $('#id_major').append(option);

            }

        } else { //valueに何も値が入っていない場合

            $('#id_major').html('');
            $('#id_major').append('<option value="" >選択してください（任意）</option>')
            $('#id_specialization').html('');
            $('#id_specialization').append('<option value="" >選択してください（任意）</option>')

        }
    })
});

/* コース・プログラムに応じて、専攻の表示を変える */

const specialization = {

    教科教育専攻: [
        '国語教育専修',
        '社会科教育専修',
        '数学教育専修',
        '理科教育専修',
        '音楽教育専修',
        '美術教育専修',
        '保健体育専修',
        '技術教育専修',
        '生活科学教育専修',
        '英語教育専修',
        '特別支援教育専修',
    ],

    特別支援教育専攻: [
        '特別支援教育専修',
    ],

}

$(document).ready(function () {
    $('#id_major').on('change', function () {

        let majorVal = $(this).val(); //選択された項目のvalueを取得

        if (majorVal) { //valueに何か値が入っていた場合

            const item = specialization[majorVal];

            $('#id_specialization').html('');

            let option;

            $('#id_specialization').append('<option value="" >選択してください（任意）</option>')
            for (let i = 0; i < item.length; i++) {

                option = '<option value="' + item[i] + '">' + item[i] + '</option>';

                $('#id_specialization').append(option);

            }

        } else { //valueに何も値が入っていない場合

            $('#id_specialization').html('');
            $('#id_specialization').append('<option value="" >選択してください（任意）</option>')

        }
    })
});

/* 学部の入力に応じて学科の表示を変える */
const subject_detail = {

    共通教育: [
        '健康運動系科目',
        '人文系',
        '社会系科目',
        '自然系科目',
        '総合科目',
        '琉大特色科目・地域創生科目',
        'キャリア関係科目',
        '情報関係科目',
        '平和共生・沖縄理解科目群',
        '外国語',
    ],

    人文社会学部専門教育: [
        '学部共通基盤科目',
        '平和共生・沖縄理解基盤科目',
        '学科基盤科目',
        '学科発展科目',
        'プログラム基盤科目',
        'プログラム発展科目',
        'プログラムコア基礎科目',
        'プログラムコア発展科目',
    ],

    国際地域創造学部専門教育: [
        '専門基盤力科目',
        '地域・国際基盤力科目（プログラム系科目）',
        '地域・国際基盤力科目（プログラム複合科目）',
        '観光地域デザインプログラム専門科目',
        '経営プログラム専門科目',
        '経営プログラム専門科目（基礎科目）',
        '経営プログラム専門科目（応用科目）',
        '経済学プログラム専門科目（基礎科目）',
        '経済学プログラム専門科目（応用科目）',
        '国際言語文化プログラム専門科目',
        '国際言語文化プログラム専門科目（基礎科目）',
        '国際言語文化プログラム専門科目（応用科目）',
        '地域文化科学プログラム専門科目',
        '地域・国際実践力科目',
    ],
}

$(document).ready(function () {
    $('#id_subject_class').on('change', function () {

        let subject_class_Val = $(this).val(); //選択された項目のvalueを取得

        if (subject_class_Val) { //valueに何か値が入っていた場合

            const item = subject_detail[subject_class_Val];

            $('#id_subject_detail').html('');

            let option;

            $('#id_subject_detail').append('<option value="" >選択してください（必須）</option>')
            for (let i = 0; i < item.length; i++) {
                option = '<option value="' + item[i] + '">' + item[i] + '</option>';
                $('#id_subject_detail').append(option);
            }

        } else { //valueに何も値が入っていない場合
            $('#id_subject_detail').html('');
            $('#id_subject_detail').append('<option value="" >選択してください（任意）</option>')
        }
    })
});