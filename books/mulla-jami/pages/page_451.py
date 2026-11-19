# -*- coding: utf-8 -*-
"""Mulla Jami — al-Fawāʾid al-Ḍiyāʾiyya. Source PDF page 451 (printed ٤٥٠)."""

PAGE_NUMBER = 451
PRINTED_PAGE = "٤٥٠"   # Arabic-Indic, as printed

BLOCKS = [
    # ---------------- The commentary text (matn) ----------------
    # Continues «… فهو أعم من أن يكون من حيث ذات» at the foot of PDF p. 450 (mid-sentence).
    {"type": "matn",
     "ar": "الواحد أو من حيث الأمور الخارجة الزائدة كما يدل عليه «ما» الإبهامية المفيدة للعموم في قوله: «بتغير ما»،",
     "en": "…of the singular or with respect to extraneous added matters, as is indicated by the indefinite “mā” conveying generality in his words “by some change”,"},
    {"type": "matn",
     "ar": "سواء كان ذلك التغير حقيقيا (كـ«رجال وأفراس») أو اعتباريا كـ«فلك»، كما مر.",
     "en": "whether that change be real (as in “rijāl” (men) and “afrās” (horses)) or notional, as in “fulk” (ship), as has passed."},

    {"type": "section", "ar": "[جمع القلة والكثرة]",
     "en": "The Plural of Paucity and the Plural of Multitude"},

    {"type": "matn",
     "ar": "(جمع القلة) وهو ما يطلق على ثلاثة وعشرة وما بينهما («أفعل») أي: جمع يكون على وزن «أفعل» كـ«أفلس» جمع فلس",
     "en": "(The plural of paucity), which is what is applied to three, ten and what lies between them, [is] (“afʿul”), that is, a plural on the pattern “afʿul”, like “aflus”, plural of “fals” (copper coin),"},
    {"type": "matn",
     "ar": "(و«أفعال»[[١]]) أي: جمع يكون على وزن «أفعال» كـ«أفراس» جمع فرس، وعلى هذا القياس معنى البواقي.",
     "en": "(and “afʿāl”), that is, a plural on the pattern “afʿāl”, like “afrās”, plural of “faras” (horse); and the meaning of the remaining ones is by this analogy."},
    {"type": "matn",
     "ar": "(و«أفعلة») كـ«أرغفة» جمع رغيف (و«فعلة») كـ«غلمة» جمع غلام.",
     "en": "(And “afʿila”), like “arghifa”, plural of “raghīf” (loaf), (and “fiʿla”), like “ghilma”, plural of “ghulām” (boy)."},
    {"type": "matn",
     "ar": "(و) الجمع (الصحيح) مذكرا كان كـ«مسلمين»، أو مؤنثا كـ«مسلمات».",
     "en": "(And the sound) plural, whether masculine, like “muslimīn”, or feminine, like “muslimāt”."},
    {"type": "matn",
     "ar": "وفي شرح الرضي: أن الظاهر أنهما أي: جمعي السلامة لمطلق الجمع من غير نظر إلى القلة والكثرة، فيصلحان لهما.",
     "en": "In the commentary of al-Raḍī [it is stated] that what is apparent is that they, that is, the two sound plurals, are for the plural as such, without regard to paucity or multitude, so they are fit for both."},
    {"type": "matn",
     "ar": "(وما عدا ذلك) المذكور من الأوزان والجمع الصحيح (جمع كثرة) يطلق على ما فوق العشرة إلى ما لا نهاية له.",
     "en": "(And whatever is other than that) mentioned, of the patterns and the sound plural, (is a plural of multitude), applied to what is above ten up to what has no limit."},
    {"type": "matn",
     "ar": "وقد يستعار أحدهما للآخر مع وجود ذلك الآخر، كقوله تعالى: ﴿ثلاثة قروء[[٢]]﴾[[٣]] مع وجود «أقراء».",
     "en": "One of them is sometimes borrowed for the other even though that other exists, as in His words, the Exalted: “three periods (qurūʾ)”, although “aqrāʾ” exists."},

    {"type": "section", "ar": "[المصدر]",
     "en": "The Verbal Noun (al-Maṣdar)"},

    {"type": "matn",
     "ar": "(المصدر: اسم الحدث[[٤]]) يعني: بالحدث معنى قائما بغيره، سواء صدر عنه كـ«الضرب والمشي»، أو لم يصدر كـ«الطول والقصر» (الجاري على الفعل).",
     "en": "(The verbal noun (maṣdar) is the noun of the event (ḥadath)), meaning by “event” a notion subsisting in something else, whether it issues from it, like “striking” and “walking”, or does not issue from it, like “tallness” and “shortness”, (which runs upon the verb)."},
    {"type": "matn",
     "ar": "والمراد بجريانه على الفعل: أن يقع بعد اشتقاق الفعل منه تأكيدا له، أو بيانا لنوعه، أو عدده مثل: «جلست جلوسا، وجلسة وجلسة»",
     "en": "What is meant by its running upon the verb is that it occurs after the verb has been derived from it, as an emphasis of it, or as a specification of its kind or of its number, as in “jalastu julūsan” (I sat a sitting), “jilsatan” (a manner of sitting) and “jalsatan” (one sitting)."},
    {"type": "matn",
     "ar": "فمثل: «القادرية والعالمية»، ومثل: «ويلا له وويحا له» مما لم يشتق الفعل منه لا يكون مصدرا، وإن كان الأخيران مفعولا مطلقا.",
     "en": "So the like of “al-qādiriyya” (being powerful) and “al-ʿālimiyya” (being knowing), and the like of “waylan lahu” (woe to him) and “wayḥan lahu” (alas for him), from which no verb is derived, are not verbal nouns, even though the latter two are absolute objects (mafʿūl muṭlaq)."},

    {"type": "rule"},

    # ---------------- Footnote 1 ----------------
    {"type": "note", "num": "١"},
    {"type": "pair",
     "ar": "في الرضي: هذه الأوزان للقلة إذا جاء للمفرد جمع كثرة.",
     "en": "In al-Raḍī: these patterns are for paucity when the singular has a plural of multitude."},
    {"type": "pair",
     "ar": "وأما إذا انحصر جمع التكسير فيها، فهي للقلة والكثرة.",
     "en": "But when the broken plural is confined to them, they are for both paucity and multitude."},
    {"type": "pair",
     "ar": "وكذا ما عدا الستة للكثرة إذا لم ينحصر فيه الجمع، وإلا فهو مشترك كأجادل ومصانع.",
     "en": "Likewise, what is other than the six is for multitude when the plural is not confined to it; otherwise it is shared [between both], as with “ajādil” (falcons) and “maṣāniʿ” (works)."},

    # ---------------- Footnote 2 ----------------
    {"type": "note", "num": "٢"},
    {"type": "pair",
     "ar": "والنكتة في ذلك التنبيه على أن ثلاثة قروء بالنسبة إلى النساء جمع كثرة لقلة صبرهن على الرجال.",
     "en": "The subtle point in this is to draw attention to the fact that three periods are, in relation to women, a plural of multitude, because of their little patience [in waiting] for men."},

    # ---------------- Footnote 3 ----------------
    {"type": "note", "num": "٣"},
    {"type": "pair",
     "ar": "سورة البقرة: ٢٢٨.",
     "en": "Qurʾān, Sūrat al-Baqara 2:228."},

    # ---------------- Footnote 4 ----------------
    {"type": "note", "num": "٤"},
    {"type": "pair",
     "ar": "أي: الموضوع له، وإن دل بسبب عارض على أمر زائد عليه كالنوعية والعددية.",
     "en": "That is, [the noun] coined for it, even if, owing to some accident, it indicates something additional to it, such as kind or number."},
]
