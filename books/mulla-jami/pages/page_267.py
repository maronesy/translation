# -*- coding: utf-8 -*-
"""Mulla Jami — al-Fawāʾid al-Ḍiyāʾiyya. Source PDF page 267 (printed ٢٦٦)."""

PAGE_NUMBER = 267
PRINTED_PAGE = "٢٦٦"   # Arabic-Indic, as printed

BLOCKS = [
    # ---------------- The commentary text (matn) ----------------
    # Continues «يتحقق في ضمن هذا الرفع الخاص في أكثر» from the foot of PDF p. 266.
    {"type": "matn",
     "ar": "المواد، وذلك لأن الإبهام فيه أكثر.",
     "en": "…cases; that is because the vagueness in it is greater."},
    {"type": "matn",
     "ar": "والمقدار: (إما) متحقق (في) ضمن (عدد نحو: «عشرون درهما») وسيأتي ذكر تمييز العدد، وبيانه في باب أسماء العدد.",
     "en": "The measure is (either) realized (in) the form of (a number, as in “twenty dirhams”); the tamyīz of number will be mentioned and explained in the chapter on numerals."},
    {"type": "matn",
     "ar": "(وإما في) ضمن (غيره) أي: غير العدد كالوزن (نحو: «رطل زيتا»)، فإن الرطل نصف المن.",
     "en": "(Or in) the form of (something else), that is, other than number, such as weight, (as in “a raṭl of oil”), for the raṭl is half a mann."},
    {"type": "matn",
     "ar": "(و) نحو: («منوان سمنا»[[١]])، وكالكيل نحو: «قفيزان برا»، وكالذراع نحو: «ذراع ثوبا».",
     "en": "(And) as in (“two manns of clarified butter”); and such as dry measure, as in “two qafīzes of wheat”; and such as the cubit, as in “a cubit of cloth.”"},
    {"type": "matn",
     "ar": "(و) كالمقياس نحو: («على التمرة مثلها زبدا»).",
     "en": "(And) such as a standard of comparison, as in (“on the date there is its like in butter”)."},
    # REVIEW: print reads «وزراع ثوبا» here (with zay), against «ذراع ثوبا» a few lines above; transcribed as printed.
    {"type": "matn",
     "ar": "والمراد بالمقادير في هذه الصور هو المقدرات؛ لأن قولك: «عندي عشرون درهما، ورطل زيتا، وزراع ثوبا، وعلى التمرة مثلها زبدا». المراد بها: المعدود، والموزون، والمذروع، والمقيس لا غير.",
     "en": "What is meant by “measures” in these forms is the things measured; for in your saying “I have twenty dirhams, a raṭl of oil, a cubit of cloth, and on the date its like in butter,” what is meant by them is the thing counted, weighed, measured by the cubit, and compared, and nothing else."},
    {"type": "matn",
     "ar": "وإنما اقتصر المصنف على الأمثلة الثلاثة[[٢]]؛ لأنه كان مطمح نظره التنبيه على بيان ما يتم به المفرد،",
     "en": "The author confined himself to the three examples only because his aim was to draw attention to what completes the single term (mufrad):"},
    {"type": "matn",
     "ar": "وهو التنوين[[٣]] كما في «رطل زيتا» والنون[[٤]] كما في «منوان سمنا»، أو الإضافة كما في «على التمرة مثلها زبدا»،",
     "en": "that is the tanwīn, as in “a raṭl of oil”; the nūn, as in “two manns of clarified butter”; or the genitive construction (iḍāfa), as in “on the date its like in butter.”"},
    {"type": "matn",
     "ar": "ولهذا لم يستوف أقسام المقادير، وكرر بعضها،",
     "en": "For this reason he did not cover all the divisions of measures, and repeated some of them."},
    {"type": "matn",
     "ar": "ومعنى تمام الاسم أن يكون على حالة لا يمكن إضافته معها،",
     "en": "The meaning of the noun’s being complete is that it be in a state in which it cannot be put into a genitive construction;"},
    {"type": "matn",
     "ar": "والاسم مستحيل الإضافة مع التنوين، ونوني التثنية والجمع، ومع الإضافة؛ لأن المضاف لا يضاف مرة ثانية[[٥]]،",
     "en": "and a noun cannot be put into a genitive construction when it has tanwīn, or the nūn of the dual or of the plural, or when it is already in a genitive construction, because a muḍāf is not made muḍāf a second time."},
    {"type": "matn",
     "ar": "فإذا تم الاسم بأحد هذه",
     "en": "So when the noun is completed by one of these…"},

    {"type": "rule"},

    # ---------------- Footnote 1 ----------------
    {"type": "note", "num": "١"},
    {"type": "pair",
     "ar": "تثنية منا بالقصر، وهو أفصح من المن بالتشديد.",
     "en": "[Manawān is] the dual of manan, with a short final alif, which is more correct than mann with a doubled nūn."},

    # ---------------- Footnote 2 ----------------
    {"type": "note", "num": "٢"},
    {"type": "pair",
     "ar": "أي: من غير العدد، وإلا فقد مثل العدد أيضا.",
     "en": "That is, [three examples] other than number; otherwise, he also gave an example of number."},
    {"type": "pair",
     "ar": "والأولى أن يبدل منوان سمنا بقفيزان برا.",
     "en": "It would have been better to replace “two manns of clarified butter” with “two qafīzes of wheat.”"},
    {"type": "pair",
     "ar": "وقوله: وهو التنوين محققا أو مقدرا كما في خمسة عشر رجلا، وكم رجلا،",
     "en": "His words “that is the tanwīn” [mean the tanwīn] whether actual or implied, as in “fifteen men” and “how many men?”"},
    {"type": "pair",
     "ar": "ويريد بما يتم به المفرد مما ينتصب التمييز، وإلا لوجب التنبيه على المعرف باللام أيضا.",
     "en": "By “what completes the single term” he means what makes the tamyīz take the accusative; otherwise he would have had to point out [the noun] made definite by the article as well."},
    {"type": "pair",
     "ar": "بقي أن من التام الناصب للتمييز التام بنفسه.",
     "en": "It remains that among complete nouns governing the tamyīz in the accusative is the noun complete in itself."},
    {"type": "pair",
     "ar": "وإنما تصدى لاستيفاء أقسام الاسم التام الناصب دون المقدار لابتناء حكم نحوي على معرفة أقسام الاسم التام،",
     "en": "He undertook to cover all the divisions of the complete governing noun, and not of measure, only because a grammatical ruling rests on knowing the divisions of the complete noun;"},
    {"type": "pair",
     "ar": "وهو ما أشار إليه بقوله: ثم إن كان بتنوين إلى آخره.",
     "en": "this is what he indicated by his words “Then if it is by tanwīn …” to the end."},
    {"type": "pair",
     "ar": "ولا يخفى أنه لو لم يفصل بين هذا الحكم وبين استيفاء الأقسام للاسم التام لكان أدخل في الانتظام.",
     "en": "It is evident that had he not separated this ruling from the full enumeration of the divisions of the complete noun, it would have been better ordered."},

    # ---------------- Footnote 3 ----------------
    {"type": "note", "num": "٣"},
    {"type": "pair",
     "ar": "لفظا أو تقديرا كما في «خمسة عشر رجلا وكم رجلا».",
     "en": "Expressed or implied, as in “fifteen men” and “how many men?”"},

    # ---------------- Footnote 4 ----------------
    {"type": "note", "num": "٤"},
    {"type": "pair",
     "ar": "سواء كان في التثنية أو شبه الجمع نحو: عشرون لا نون الجمع، نحو: حسنون وجها؛ لأن التمييز فيه يكون عن ذات مقدرة.",
     "en": "Whether in the dual or in what resembles the plural, as in “twenty,” but not the nūn of the plural, as in “ḥasanūna wajhan” (handsome in face); for the tamyīz there is from an implied entity."},

    # ---------------- Footnote 5 ----------------
    {"type": "note", "num": "٥"},
    {"type": "pair",
     "ar": "لأن الاسم لا يضاف إلى الاسمين بدون عاطف، وإن أضيف مع حذف المضاف إليه لزم خلاف المفروض.",
     "en": "Because a noun is not put in a genitive construction with two nouns without a conjunction; and if it were so construed with the [first] muḍāf ilayhi elided, the contrary of the supposition would follow."},
]
