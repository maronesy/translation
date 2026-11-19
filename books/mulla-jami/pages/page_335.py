# -*- coding: utf-8 -*-
"""Mulla Jami — al-Fawāʾid al-Ḍiyāʾiyya. Source PDF page 335 (printed ٣٣٤)."""

PAGE_NUMBER = 335
PRINTED_PAGE = "٣٣٤"   # Arabic-Indic, as printed

BLOCKS = [
    # ---------------- The commentary text (matn) ----------------
    # Continues «… لأن» at the foot of PDF p. 334.
    {"type": "matn",
     "ar": "تعريف المضاف مساو لتعريف المضاف إليه أو أنقص منه[[١]]، على الخلاف الواقع بين سيبويه وغيره،",
     "en": "…the definiteness of the annexed noun (al-muḍāf) is equal to the definiteness of the noun to which it is annexed (al-muḍāf ilayhi), or less than it, according to the disagreement between Sībawayh and others;"},
    {"type": "matn",
     "ar": "بخلاف سائر المعارف، فإنها أخص من ذي اللام، فلو وقع أخص نعتا لغير أخص، فهو محمول على البدل عند صاحب هذا المذهب.",
     "en": "unlike the other definite nouns (maʿārif), for they are more specific than the noun with the article; so if a more specific noun occurred as an epithet (naʿt) of one that is not more specific, it is construed as a substitute (badal) by the holder of this doctrine."},
    {"type": "matn",
     "ar": "(وإنما التزم وصف باب هذا) أي: باب اسم الإشارة (بذي اللام[[٢]]) مثل: «مررت بهذا الرجل»",
     "en": "(The qualification of the category of hādhā), that is, the category of the demonstrative noun (ism al-ishāra), (by a noun with the article was made obligatory only), as in “marartu bi-hādhā al-rajul” (I passed by this man),"},
    {"type": "matn",
     "ar": "مع أن القياس يقتضي[[٣]] جواز وصفه بذي اللام والموصول والمضاف إلى أحدهما (للإبهام) الواقع في هذا الباب بحسب أصل الوضع المقتضي لبيان الجنس،",
     "en": "although analogy (qiyās) requires that it may be qualified by a noun with the article, by the relative noun (mawṣūl), and by a noun annexed to one of these two, (because of the vagueness) (ibhām) that belongs to this category by its original coinage (aṣl al-waḍʿ), which calls for the genus to be made clear."},
    {"type": "matn",
     "ar": "فإذا أريد رفعه لا يتصور بمثله لإبهامه، ولا يليق بالمضاف المكتسب التعريف من المضاف إليه؛ لأنه كالاستعارة من المستعير والسؤال من المحتاج الفقير،",
     "en": "When its removal is intended, this cannot be conceived through its like, because of the latter’s vagueness; nor does it suit the annexed noun that acquires its definiteness from the noun to which it is annexed, for that is like borrowing from a borrower and asking of one who is himself needy and poor."},
    {"type": "matn",
     "ar": "فتعين ذو اللام، لتعينه في نفسه وحمل الموصول عليه؛ لأنه مع صلته مثل ذي اللام، مثل: «مررت بهذا الذي كرم» أي: الكريم.",
     "en": "So the noun with the article was determined, because it is determinate in itself; and the relative noun is assimilated to it, since together with its relative clause (ṣila) it is like a noun with the article, as in “marartu bi-hādhā alladhī karuma” (I passed by this one who is noble), that is, al-karīm (the noble one)."},
    {"type": "matn",
     "ar": "(ومن ثمة) أي: ومن أجل أن التزام وصف باب هذا بذي اللام لرفع الإبهام المقتضي لبيان الجنس (ضعف «مررت بهذا الأبيض»)؛",
     "en": "(Hence), that is, because the obligatory qualification of the category of hādhā by a noun with the article serves to remove the vagueness that calls for the genus to be made clear, (“marartu bi-hādhā al-abyaḍ” [I passed by this white one] is weak),"},
    {"type": "matn",
     "ar": "لأنه لا يتبين به جنس المبهم؛ لأن الأبيض عام لا يختص بجنس دون جنس",
     "en": "since the genus of the vague noun is not made clear by it, for “white” is general and is not specific to one genus rather than another;"},
    {"type": "matn",
     "ar": "(وحسن «مررت بهذا العالم»)؛ لأنه يتبين به أن المشار إليه إنسان[[٤]] بل رجل[[٥]].",
     "en": "(and “marartu bi-hādhā al-ʿālim” [I passed by this learned one] is good), since it makes clear that the one pointed to is a human being, indeed a man."},

    {"type": "section", "ar": "[العطف]",
     "en": "Conjunction (al-ʿAṭf)"},

    {"type": "matn",
     "ar": "(العطف[[٦]]) يعني: المعطوف بالحرف: (تابع مقصود) أي: قصد نسبته[[٧]] إلى شيء أو نسبة شيء إليه (بالنسبة) الواقعة في الكلام[[٨]].",
     "en": "(Conjunction) (al-ʿaṭf), meaning the noun conjoined by a particle, (is a dependent [tābiʿ] that is intended), that is, whose attribution to something, or the attribution of something to it, is intended, (by the attribution) (al-nisba) occurring in the utterance."},

    {"type": "rule"},

    # ---------------- Footnote 1 ----------------
    {"type": "note", "num": "١"},
    {"type": "pair",
     "ar": "ينبغي أن يدعى أن الأنقص لا ينحط إلى درجة ما هو دون المضاف إليه حتى يثبت المدعى.",
     "en": "It should be claimed that the less [definite annexed noun] does not sink to the rank of what is below the noun to which it is annexed, so that the claim is established."},

    # ---------------- Footnote 2 ----------------
    {"type": "note", "num": "٢"},
    {"type": "pair",
     "ar": "يجب أن يراد بذي اللام ما يشمل الذي وأخواته.",
     "en": "By “the noun with the article” must be meant what includes alladhī and its sisters."},
    {"type": "pair",
     "ar": "قال الرضي: لا يوصف اسم الإشارة إلا بذي اللام والموصول نحو: بهذا الرجل، وبهذا الذي قال كذا، وبهذا ذي قال كذا على لغة الطائية، هذا كلامه.",
     "en": "Al-Raḍī said: “The demonstrative noun is qualified only by a noun with the article and by the relative noun, as in ‘bi-hādhā al-rajul’, ‘bi-hādhā alladhī qāla kadhā’ (by this one who said such), and ‘bi-hādhā dhī qāla kadhā’ in the dialect of Ṭayyiʾ.” These are his words."},
    {"type": "pair",
     "ar": "والأظهر أن يراد بهذا في قوله باب هذا خصوصه، وبقوله: باب هذا اسم الإشارة إلا أن يراد بهذا اسم الإشارة، فتأمل.",
     "en": "The more evident reading is that by hādhā in his words “the category of hādhā” its particular [word] is meant, and by his words “the category of hādhā” the demonstrative noun [is meant] only if by hādhā the demonstrative noun is meant; so reflect."},

    # ---------------- Footnote 3 ----------------
    {"type": "note", "num": "٣"},
    {"type": "pair",
     "ar": "وبمثله من أسماء الإشارة، وبالمضاف إلى مثله.",
     "en": "[It requires that it may be qualified] also by its like among the demonstrative nouns, and by a noun annexed to its like."},

    # ---------------- Footnote 4 ----------------
    {"type": "note", "num": "٤"},
    {"type": "pair",
     "ar": "بدليل الإشارة والمرور.",
     "en": "As shown by the pointing and by the passing by."},

    # ---------------- Footnote 5 ----------------
    {"type": "note", "num": "٥"},
    {"type": "pair",
     "ar": "بقرينة تذكير اسم الإشارة والصفة.",
     "en": "By the indication of the masculine gender of the demonstrative noun and of the qualifier."},

    # ---------------- Footnote 6 ----------------
    {"type": "note", "num": "٦"},
    {"type": "pair",
     "ar": "هو في اللغة: الإمالة. لقب هذا القسم من التوابع به لإمالة حرف العطف ما بعده إلى ما قبله.",
     "en": "Lexically it means inclining (imāla). This class of dependents was named by it because the conjunctive particle inclines what follows it toward what precedes it."},
    {"type": "pair",
     "ar": "ويسمى أيضا بعطف النسق؛ لأنه يكون مع متبوعه على نسق واحد؛ لأن كلا منهما مقصود بالنسبة.",
     "en": "It is also called ʿaṭf al-nasaq (coordinating conjunction), because it stands with the noun it follows (matbūʿ) in a single order (nasaq), since each of them is intended by the attribution."},

    # ---------------- Footnote 7 ----------------
    {"type": "note", "num": "٧"},
    {"type": "pair",
     "ar": "في صدقه على مثل: البيت سقف وجدران خفاء.",
     "en": "There is obscurity in its applying to such as “al-bayt saqf wa-judrān” (the house is a roof and walls)."},

    # ---------------- Footnote 8 ----------------
    {"type": "note", "num": "٨"},
    {"type": "pair",
     "ar": "أي: في الكلام الذي فيه متبوعه لئلا ينتقض بـ«جاء زيد أخوك» لا غير أو «جاء زيد وعمر»،",
     "en": "That is, in the utterance in which the noun it follows occurs, so that [the definition] is not broken by “jāʾa Zaydun akhūka lā ghayr” (Zayd, your brother, came, and none other) or “jāʾa Zaydun wa-ʿAmr” (Zayd and ʿAmr came);"},
    {"type": "pair",
     "ar": "فإن «أخوك» وإن كان مقصودا بالنسبة مع متبوعه وهو «زيد»، لكن لا في الكلام الذي فيه «زيد».",
     "en": "for “akhūka”, though it is intended by the attribution together with the noun it follows, namely “Zayd”, is not so in the utterance in which “Zayd” occurs."},
]
