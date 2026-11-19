# -*- coding: utf-8 -*-
"""Mulla Jami — al-Fawāʾid al-Ḍiyāʾiyya. Source PDF page 201 (printed ٢٠٠)."""

PAGE_NUMBER = 201
PRINTED_PAGE = "٢٠٠"   # Arabic-Indic, as printed

BLOCKS = [
    # ---------------- The commentary text (matn) ----------------
    {"type": "matn",
     "ar": "(ويبنى) أي: المنادى، قدم بيان البناء والخفض والفتح على النصب؛ لقلتها[[١]] بالنسبة إلى النصب،",
     "en": "(And it is made indeclinable—wa-yubnā), that is, the munādā. He put the account of indeclinability (bināʾ), the genitive and the fatḥa before the accusative because they are few relative to the accusative,"},
    {"type": "matn",
     "ar": "ولطلب الاختصار في بيان النصب[[٢]] بقوله: «وينصب ما سواهما»",
     "en": "and to seek concision in stating the accusative, by his words “and what is other than these two is put in the accusative.”"},
    {"type": "matn",
     "ar": "(على ما يرفع به[[٣]]) أي: على «الضمة[[٤]]، أو الألف، أو الواو» التي يرفع بها المنادى في غير صورة النداء[[٥]]",
     "en": "(On that by which it is put in the nominative—ʿalā mā yurfaʿu bihi), that is: on “the ḍamma, or the alif, or the wāw” by which the munādā is put in the nominative outside the vocative form;"},
    {"type": "matn",
     "ar": "أو الفعل مسند[[٦]] إلى الجار والمجرور أعني: «به» ولا ضمير فيه،",
     "en": "or the verb is predicated of the preposition and its object, I mean “bihi,” and there is no pronoun in it;"},
    {"type": "matn",
     "ar": "وإرجاع الضمير إلى الاسم غير ملائم لسوق الكلام[[٧]].",
     "en": "and referring the pronoun back to the noun does not suit the drift of the discourse."},
    {"type": "matn",
     "ar": "(إن كان) أي: المنادى (مفردا) أي: لا يكون مضافا[[٨]] ولا شبه مضاف[[٩]]،",
     "en": "(If it is), that is, the munādā, (single—mufradan), that is: it is neither annexed (muḍāf) nor resembling the annexed (shibh muḍāf);"},
    {"type": "matn",
     "ar": "وهو كل اسم[[١٠]] لا يتم معناه إلا بانضمام أمر آخر إليه",
     "en": "and that [resembling the annexed] is every noun whose meaning is completed only by joining something else to it;"},
    {"type": "matn",
     "ar": "(معرفة) قبل النداء[[١١]] أو بعده،",
     "en": "(definite—maʿrifatan), before the vocative or after it."},
    {"type": "matn",
     "ar": "وإنما بني المفرد المعرفة؛ لوقوعه موقع الكاف الاسمية[[١٢]] المشابهة لفظا ومعنى لكاف الخطاب",
     "en": "The single definite [munādā] was made indeclinable only because it occurs in the position of the nominal kāf, which resembles in form and meaning the kāf of address…"},

    {"type": "rule"},

    # ---------------- Footnote 1 ----------------
    {"type": "note", "num": "١"},
    {"type": "pair",
     "ar": "باعتبار المحل، فإن محلها اثنان: مفرد معرفة ومستغاث بخلاف محال النصب، فإنها ثلاثة،",
     "en": "With respect to their places: for their places are two—the single definite and the one called for help (mustaghāth)—unlike the places of the accusative, which are three;"},
    {"type": "pair",
     "ar": "أو لقلتها بحسب التحقيق والاستعمال، وفيه خدشة.",
     "en": "or because they are few in actual occurrence and usage; and there is a flaw in this."},

    # ---------------- Footnote 2 ----------------
    {"type": "note", "num": "٢"},
    {"type": "pair",
     "ar": "الذي هو كثير يناسب فيه الاختصار والضبط، وإلا لو عكس الأمر وفصل النصب والخفض والفتح.",
     "en": "[The accusative,] which is frequent, so that concision and precise delimitation suit it; otherwise, he would have reversed the matter and detailed the accusative, the genitive and the fatḥa."},
    {"type": "pair",
     "ar": "ثم قيل: ويبنى على ما يرفع به فيما سوى ذلك لحصل الاختصار في المبني على ما يرفع به.",
     "en": "Then it would have been said: “and it is made indeclinable on that by which it is put in the nominative in what is other than that,” and concision would have been achieved in [stating] what is made indeclinable on that by which it is put in the nominative."},

    # ---------------- Footnote 3 ----------------
    {"type": "note", "num": "٣"},
    {"type": "pair",
     "ar": "أي: بالضرورة لا بالإمكان العام،",
     "en": "That is: necessarily, not by general possibility (al-imkān al-ʿāmm)."},
    {"type": "pair",
     "ar": "لا يقال: فينتقض الحكم بالعلم الموصوف بـ«ابن» مضاف إلى علم آخر؛ لأن ذكره فيما بعد بمنزلة الاستثناء.",
     "en": "It should not be said: “the rule is then broken by a proper name qualified by ‘ibn’ annexed to another proper name,” because his mentioning it later is equivalent to an exception."},

    # ---------------- Footnote 4 ----------------
    {"type": "note", "num": "٤"},
    {"type": "pair",
     "ar": "لفظا أو تقديرا كما في المقصور والمنقوص، والمبني قبل النداء مثل: يا هذا، ويا هؤلاء، ويا أنت.",
     "en": "Explicitly or by implication, as in the noun ending in alif maqṣūra (maqṣūr), the defective noun (manqūṣ), and what is indeclinable before the vocative, like “yā hādhā,” “yā hāʾulāʾi” and “yā anta.”"},
    {"type": "pair",
     "ar": "وجوز أيضا يا إياك نظرا إلى كونه مفعولا.",
     "en": "“Yā iyyāka” was also allowed, in view of its being an object."},
    {"type": "pair",
     "ar": "وإذا اضطر إلى تنوين المنادى المضموم اقتصر على قدر الضرورة.",
     "en": "When one is compelled [in verse] to give tanwīn to the munādā marked with ḍamma, one limits oneself to the measure of the necessity."},

    # ---------------- Footnote 5 ----------------
    {"type": "note", "num": "٥"},
    {"type": "pair",
     "ar": "يعني: أنه من قبيل «أرضعت هذه المرأة هذا الشاب».",
     "en": "He means that it is of the type of “This woman suckled this young man.”"},

    # ---------------- Footnote 6 ----------------
    {"type": "note", "num": "٦"},
    {"type": "pair",
     "ar": "عطف بحسب المعنى؛ إذ كأنه قال: الفعل مسند إلى ضمير المنادى، أو الفعل مسند إلى الجار والمجرور.",
     "en": "A coordination according to the sense, since it is as though he said: “the verb is predicated of the pronoun of the munādā, or the verb is predicated of the preposition and its object.”"},

    # ---------------- Footnote 7 ----------------
    {"type": "note", "num": "٧"},
    {"type": "pair",
     "ar": "لأن الكلام مسوق لبيان المنادى؛ لكنه خال عن التكلف الذي في رجوع الضمير إلى المنادى.",
     "en": "Because the discourse is directed to explaining the munādā; but it is free of the strain involved in referring the pronoun back to the munādā."},

    # ---------------- Footnote 8 ----------------
    {"type": "note", "num": "٨"},
    {"type": "pair",
     "ar": "بالإضافة المعنوية، ولا شبه مضاف. ويندرج فيه الإضافة باللفظية.",
     "en": "By semantic annexation (al-iḍāfa al-maʿnawiyya), nor resembling the annexed. Annexation by the verbal [annexation] is included in it."},

    # ---------------- Footnote 9 ----------------
    {"type": "note", "num": "٩"},
    {"type": "pair",
     "ar": "يعني: إن المفرد مقابل للمضاف، لكن أريد الفرد الكامل منه، فيخرج شبه المضاف أيضا.",
     "en": "He means: the single is the counterpart of the annexed, but its complete instance is intended, so that what resembles the annexed is also excluded."},
    {"type": "pair",
     "ar": "أما إخراج المنادى المجرور باللام أو المفتوح بالألف بتلك الإرادة، فبعيد.",
     "en": "As for excluding, by that intention, the munādā in the genitive by the lām or the one given fatḥa with the alif, that is far-fetched."},

    # ---------------- Footnote 10 ----------------
    {"type": "note", "num": "١٠"},
    {"type": "pair",
     "ar": "هذا مأخوذ من الضابطة التي ذكرها الشيخ الرضي للمشبه بالمضاف،",
     "en": "This is taken from the criterion that Shaykh al-Raḍī gave for what resembles the annexed,"},
    {"type": "pair",
     "ar": "وهي كل اسم يجيء أمر بعده من تمامه من حيث المعنى، لكن لا انضباط لها في شيء،",
     "en": "namely: every noun after which comes something that completes it in meaning. But it is not exact in anything,"},
    {"type": "pair",
     "ar": "فإنهم قالوا: إن الموصوف بجملة أو ظرف شبه مضاف في باب النداء، مثل: «يا مقيما» دون باب \"لا\" التي لنفي الجنس.",
     "en": "for they said that what is qualified by a sentence or an adverbial (ẓarf) resembles the annexed in the section on the vocative, as in “yā muqīman,” but not in the section on the “lā” that negates the genus."},

    # ---------------- Footnote 11 ----------------
    {"type": "note", "num": "١١"},
    {"type": "pair",
     "ar": "لا يقال: يلزم اجتماع التعريفين، وهو ممتنع؛ لأنا نقول: الممتنع اجتماع آلتي التعريف.",
     "en": "It should not be said: “two determinations then come together, which is impossible,” because we say: what is impossible is that two instruments of determination come together."},
    {"type": "pair",
     "ar": "لا يقال: يلزم ذلك الاجتماع في المنادى المضاف إلى المعرفة؛ لأنا نقول: صورة الإضافة ليست نصا في التعريف مع أن محل الدخول مختلف.",
     "en": "It should not be said: “that coming together then follows in the munādā annexed to a definite noun,” because we say: the form of annexation is not explicit in determination, besides the fact that the place where [each] enters differs."},

    # ---------------- Footnote 12 ----------------
    {"type": "note", "num": "١٢"},
    {"type": "pair",
     "ar": "اعلم أن الأسماء المظهرة مما لا خطاب فيها؛ إذ هي كلها غيب،",
     "en": "Know that explicit nouns (al-asmāʾ al-muẓhara) are among the things that contain no address, since they are all of the third person (ghayb);"},
    {"type": "pair",
     "ar": "إلا أنه لما سرى إليه الخطاب بواسطة حرف النداء جرى مجرى المضمر الذي وضع للخطاب، وصار في حكمه.",
     "en": "but when address extended to it by means of the vocative particle, it was treated like the pronoun coined for address and took its status."},
    {"type": "pair",
     "ar": "وإنما عدلوا عن الأصل",
     "en": "They departed from the original [rule] only…"},
]
