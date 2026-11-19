# -*- coding: utf-8 -*-
"""Mulla Jami — al-Fawāʾid al-Ḍiyāʾiyya. Source PDF page 290 (printed ٢٨٩)."""

PAGE_NUMBER = 290
PRINTED_PAGE = "٢٨٩"   # Arabic-Indic, as printed

BLOCKS = [
    # ---------------- The commentary text (matn) ----------------
    # Continues «نصبوه استنكارا لرفعه،» from the foot of PDF p. 289.
    {"type": "matn",
     "ar": "فيقولون: «جاءني سواءك، وفي الدار سواءك»،",
     "en": "…so they say “Someone other than you [sawāʾaka] came to me,” and “In the house is someone other than you [sawāʾaka].”"},
    {"type": "matn",
     "ar": "ومثل هذا في استنكار الرفع فيما غلب انتصابه عن الظرفية قوله تعالى: ﴿لقد تقطع بينكم﴾[[١]] بالنصب.",
     "en": "Similar to this, in finding the nominative objectionable in what is mostly accusative as an adverb, is the saying of the Exalted, “Indeed [the bond] between you [baynakum] has been severed,” with the accusative."},

    {"type": "section", "ar": "[خبر كان وأخواتها]",
     "en": "The Predicate of Kāna and Its Sisters"},

    {"type": "matn",
     "ar": "(خبر كان وأخواتها) وستعرفها[[٢]] في قسم الفعل -إن شاء الله تعالى- (هو المسند بعد دخولها) أي: دخول «كان» أو إحدى أخواتها.",
     "en": "(The predicate of kāna and its sisters)—you will come to know them in the section on the verb, if Allah the Exalted wills—(is what is predicated after their entry), that is, after the entry of “kāna” or one of its sisters."},
    {"type": "matn",
     "ar": "والمراد ببعدية المسند[[٣]] لدخولها أن يكون إسناده إلى اسمها واقعا بعد دخولها على اسمها وخبرها،",
     "en": "What is meant by the predicated thing’s coming after their entry is that its attribution (isnād) to their noun (ism) occurs after their entry upon their noun and predicate;"},
    {"type": "matn",
     "ar": "ولا شك أن ذلك إنما يتصور بعد تقرر الاسم والخبر،",
     "en": "and there is no doubt that this is conceivable only after the noun and the predicate are established."},
    {"type": "matn",
     "ar": "فالإسناد الواقع بين أجزاء الخبر[[٤]] المقدم على تقرره لا يكون بعد دخولها، بل يكون قبله،",
     "en": "So the attribution occurring among the parts of the predicate, which precedes its establishment, is not after their entry but before it;"},
    {"type": "matn",
     "ar": "فلا ينتقض التعريف بمثل: «كان زيد يضرب أبوه»، ولا بمثل: «كان زيد أبوه قائم»،",
     "en": "so the definition is not refuted by such as “Zayd was [such that] his father strikes,” nor by such as “Zayd was [such that] his father is standing,”"},
    {"type": "matn",
     "ar": "بأن يقال: يصدق على «يضرب» و«قائم» في هذين المثالين المعرف، وليسا من أفراد المعرف.",
     "en": "by its being said: the thing defined applies to “yaḍribu” and “qāʾimun” in these two examples, yet they are not among the instances of the thing defined."},
    {"type": "matn",
     "ar": "ويمكن أن يقال في جواب هذا النقض: إن المراد بدخولها ورودها للعمل فيما وردت عليه كما سبقت الإشارة إليه في خبر «إن» وأخواتها",
     "en": "It may be said in answer to this objection: what is meant by their entry is their coming in to govern what they come upon, as was indicated under the predicate of “inna” and its sisters;"},
    {"type": "matn",
     "ar": "(مثل: «كان زيد قائما»).",
     "en": "(as in “Zayd was standing”)."},
    {"type": "matn",
     "ar": "(وأمره) أي: أمر خبر «كان» وأخواتها (كأمر خبر المبتدأ) في أقسامه وأحكامه وشرائطه على ما سبق في بحث المبتدأ والخبر.",
     "en": "(Its status), that is, the status of the predicate of “kāna” and its sisters, (is like the status of the predicate of the mubtadaʾ) in its divisions, rules and conditions, as given in the discussion of the mubtadaʾ and khabar."},
    {"type": "matn",
     "ar": "(و) لكنه (يتقدم) على اسمها حال كونه (معرفة[[٥]]) حقيقة أو حكما كالنكرة المخصصة،",
     "en": "(But) it (may precede) their noun while being (definite), really or virtually, like a specified indefinite noun,"},
    {"type": "matn",
     "ar": "لاختلاف اسمها وخبرها في الإعراب، فلا يلتبس أحدهما بالآخر،",
     "en": "because their noun and predicate differ in inflection, so neither is confused with the other;"},
    {"type": "matn",
     "ar": "وذلك إذا كان الإعراب فيهما أو في أحدهما لفظيا نحو: «كان المنطلق زيد»، و«كان هذا",
     "en": "that is when the inflection in both, or in one of them, is overt (lafẓī), as in “Zayd was the one departing,” and “This was…"},

    {"type": "rule"},

    # ---------------- Footnote 1 ----------------
    {"type": "note", "num": "١"},
    {"type": "pair",
     "ar": "سورة الأنعام: ٩٤.",
     "en": "(Qurʾān, Sūrat al-Anʿām 6:94)."},

    # ---------------- Footnote 2 ----------------
    {"type": "note", "num": "٢"},
    {"type": "pair",
     "ar": "أي: أخواتها. ولهذا لم يبينها المصنف.",
     "en": "That is, its sisters; for this reason the author did not set them out."},
    {"type": "pair",
     "ar": "ولك أن تجعل ضمير «وستعرفها» إلى كان وأخواتها؛ لأن كان التي يثبت لها الخبر لم يعرف بعد.",
     "en": "You may also refer the pronoun of “you will come to know them” to kāna and its sisters together, because the kāna to which a predicate belongs has not yet been made known."},

    # ---------------- Footnote 3 ----------------
    {"type": "note", "num": "٣"},
    {"type": "pair",
     "ar": "أراد باسمها وخبرها ما يصير اسمها وخبرها.",
     "en": "By “their noun and predicate” he meant what becomes their noun and predicate."},
    {"type": "pair",
     "ar": "والأظهر في العبارة أن يقال: المراد ببعدية المسند لدخولها أن يكون إسناده واقعا بعد دخولها.",
     "en": "The clearer wording would be: what is meant by the predicated thing’s coming after their entry is that its attribution occurs after their entry."},

    # ---------------- Footnote 4 ----------------
    {"type": "note", "num": "٤"},
    {"type": "pair",
     "ar": "لا يقال: وكذا الإسناد الواقع بين الخبر والاسم بناء على أنها تدخل الجملة الاسمية؛ لأنا نقول: ذلك الإسناد قد غير بدخولها.",
     "en": "It cannot be said: likewise the attribution between the predicate and the noun [precedes their entry], since they enter upon a nominal sentence; for we say: that attribution has been altered by their entry."},

    # ---------------- Footnote 5 ----------------
    {"type": "note", "num": "٥"},
    {"type": "pair",
     "ar": "لما كان يتجه عليه أن المخالفة بخبر المبتدأ لا يخص ذلك، بل يتقدم نكرة مخصصة أيضا تكلف الشارح لدفعه بقوله: حقيقة أو حكما.",
     "en": "Since the objection could be raised against it that the difference from the predicate of the mubtadaʾ is not confined to this—rather, it also precedes when a specified indefinite—the commentator took pains to remove it with his words “really or virtually.”"},
]
