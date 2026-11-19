# -*- coding: utf-8 -*-
"""Mulla Jami — al-Fawāʾid al-Ḍiyāʾiyya. Source PDF page 282 (printed ٢٨١)."""

PAGE_NUMBER = 282
PRINTED_PAGE = "٢٨١"   # Arabic-Indic, as printed

BLOCKS = [
    # ---------------- The commentary text (matn) ----------------
    # Continues «ولم يشترط ألا يكون منقطعا ولا مقدما على المستثنى منه؛ لأن» from PDF p. 281.
    {"type": "matn",
     "ar": "حكمهما قد علم فيما سبق، فاكتفى بذلك",
     "en": "…their ruling has been learned from what preceded, so he was content with that."},
    {"type": "matn",
     "ar": "(نحو: ﴿ما فعلوه إلا قليل﴾[[١]]) بالرفع على البدلية[[٢]] (و«إلا قليلا») بالنصب على الاستثناء،",
     "en": "(As in: “They would not have done it, except a few” [illā qalīlun]), in the nominative as a substitute, (and “illā qalīlan”), in the accusative as an exception;"},
    {"type": "matn",
     "ar": "ونحو: «ما مررت بأحد إلا زيد» بالجر على البدلية، و«إلا زيدا» بالنصب على الاستثناء،",
     "en": "and as in “I did not pass by anyone except Zayd” [illā Zaydin], in the genitive as a substitute, and “illā Zaydan,” in the accusative as an exception;"},
    {"type": "matn",
     "ar": "و«ما رأيت أحدا إلا زيدا» بالنصب إما بطريق البدلية وهو المختار، أو بطريق الاستثناء، وهو جائز غير مختار،",
     "en": "and “I did not see anyone except Zayd,” in the accusative, either by way of substitution, which is the preferred [analysis], or by way of exception, which is permissible but not preferred."},
    {"type": "matn",
     "ar": "وإنما اختاروا البدل في هذه الصور؛ لأن النصب على الاستثناء إنما هو بسبب التشبيه بالمفعول لا بالأصالة[[٣]]، وبواسطة «إلا»، وإعراب البدل بالأصالة[[٤]] وبغير واسطة.",
     "en": "They preferred the substitute in these cases only because the accusative as an exception is by reason of resemblance to the object, not originally, and through the mediation of “illā,” whereas the inflection of the substitute is original and without mediation."},
    {"type": "matn",
     "ar": "(ويعرب) أي: المستثنى (على حسب العوامل[[٥]]) أي: بما يقتضيه العامل من الرفع والنصب والجر (إذا كان المستثنى منه غير مذكور[[٦]])",
     "en": "(And it is inflected), that is, the excepted term, (according to the governors), that is, with what the governor requires of nominative, accusative and genitive, (when the mustathnā minhu is not mentioned);"},
    {"type": "matn",
     "ar": "ويختص ذلك المستثنى باسم المفرغ؛ لأنه فرغ له العامل عن المستثنى منه، فالمراد بالمفرغ المفرغ له[[٧]]، كما يراد بالمشترك المشترك فيه",
     "en": "that excepted term is distinguished by the name “emptied” (mufarragh), because the governor has been emptied for it of the mustathnā minhu; so by “mufarragh” is meant “that for which [the governor] is emptied,” just as by “mushtarak” (shared) is meant “that in which [things] share,”"},
    {"type": "matn",
     "ar": "(وهو) أي: والحال أن المستثنى[[٨]] واقع (في غير) الكلام",
     "en": "(and it), that is, the situation being that the excepted term occurs (in other than) [affirmative] speech…"},

    {"type": "rule"},

    # ---------------- Footnote 1 ----------------
    {"type": "note", "num": "١"},
    {"type": "pair",
     "ar": "سورة النساء: ٦٦.",
     "en": "Qurʾān, Sūrat al-Nisāʾ 4:66."},

    # ---------------- Footnote 2 ----------------
    {"type": "note", "num": "٢"},
    {"type": "pair",
     "ar": "أراد بدل البعض من الكل.",
     "en": "He meant the substitute of the part for the whole (badal al-baʿḍ min al-kull)."},
    # REVIEW: print reads «يعني غناء الضمير»; the sense suggests «يغني غناء الضمير» (it suffices in place of the pronoun). Transcribed as printed.
    {"type": "pair",
     "ar": "وإنما يصح ذلك مع انتفاء ضمير المبدل منه فيه؛ لأن الاستثناء المتصل يعني غناء الضمير؛ لأنه يفيد أن المستثنى بعض من المستثنى منه.",
     "en": "This is valid despite the absence in it of a pronoun referring to the mubdal minhu only because the conjoined exception does the work of the pronoun, since it conveys that the excepted term is part of the mustathnā minhu."},

    # ---------------- Footnote 3 ----------------
    {"type": "note", "num": "٣"},
    {"type": "pair",
     "ar": "أي: بنوع تمحل.",
     "en": "That is, by a kind of contrivance."},

    # ---------------- Footnote 4 ----------------
    {"type": "note", "num": "٤"},
    {"type": "pair",
     "ar": "المراد بالأصالة ليس ما يقابل التبعية.",
     "en": "What is meant by “originally” is not what stands opposite to dependency (tabaʿiyya)."},

    # ---------------- Footnote 5 ----------------
    {"type": "note", "num": "٥"},
    {"type": "pair",
     "ar": "أي: على قدر العوامل، فإن العوامل ثلاثة: عامل الرفع، والنصب، والجر.",
     "en": "That is, in proportion to the governors; for the governors are three: the governor of the nominative, of the accusative and of the genitive."},
    {"type": "pair",
     "ar": "فالإعراب على قدرها كناية عن الإعراب بالرفع والنصب والجر.",
     "en": "So inflection in proportion to them is an allusion (kināya) to inflection with nominative, accusative and genitive."},
    # REVIEW: print reads «احتيار» (undotted ḥāʾ); evidently «اختيار» (choosing). Transcribed as printed.
    {"type": "pair",
     "ar": "وبهذا اندفع أن المراد إن كان عامل المستثنى منه يشكل بقولنا: ما مررت إلا بزيد، فإنه معرب بعامل نفسه، وإن كان المراد عامل المستثنى، فكل مستثنى معرب على حسب عامله على أنه يمكن احتيار الشق الأول أيضا.",
     "en": "By this is repelled [the objection]: if what is meant is the governor of the mustathnā minhu, it is problematic in view of our saying “I passed by none but Zayd,” for that is inflected by its own governor; and if what is meant is the governor of the excepted term, then every excepted term is inflected according to its governor. Moreover, choosing the first alternative is also possible."},
    {"type": "pair",
     "ar": "ويقال: الجار في «بزيد» عامل المستثنى منه انتقل إلى المستثنى بعد حذفه، فهو معرب بعامل المستثنى منه لا بعامله، وعامله الفعل بواسطة «إلا».",
     "en": "It may be said: the preposition in “bi-Zayd” is the governor of the mustathnā minhu, which passed over to the excepted term after [the mustathnā minhu] was elided; so it is inflected by the governor of the mustathnā minhu, not by its own governor, its own governor being the verb through the mediation of “illā.”"},

    # ---------------- Footnote 6 ----------------
    {"type": "note", "num": "٦"},
    {"type": "pair",
     "ar": "قال الشيخ الرضي: إنما أعرب حينئذ بإعراب المستثنى منه؛ لأن المنسوب إليه هو المجموع المركب من المستثنى منه والمستثنى.",
     "en": "Shaykh al-Raḍī said: it is inflected in that case with the inflection of the mustathnā minhu only because that to which [the predicate] is attributed is the compound whole made up of the mustathnā minhu and the excepted term."},
    {"type": "pair",
     "ar": "وإنما أعرب المستثنى منه بما يقتضيه المنسوب؛ لأنه الجزء الأول والمستثنى صار بعده في حيز الفضلات، فأعرب النصب",
     "en": "The mustathnā minhu is inflected with what the attributed [term] requires only because it is the first part, and the excepted term, coming after it, fell within the domain of the supplementary elements (faḍalāt); so it was inflected with the accusative."},
    {"type": "pair",
     "ar": "يعني: فإذا أخذ المستثنى منه لم يبق المستثنى في حيز الفضلات، فأعطي ما هو حقه من الإعراب لانتفاء الجزء الأول.",
     "en": "He means: when the mustathnā minhu is removed, the excepted term no longer remains within the domain of the supplementary elements, so it is given the inflection that is its due, because the first part is absent."},

    # ---------------- Footnote 7 ----------------
    {"type": "note", "num": "٧"},
    {"type": "pair",
     "ar": "يعني: المفرغ مما حذف فيه الجار، وأوصل الضمير المجرور به.",
     "en": "He means: “mufarragh” is among the cases in which the preposition has been elided and the pronoun in the genitive by it joined [directly]."},
    {"type": "pair",
     "ar": "ولك أن تستغنى عن هذا التكلف بأن تجعل المفرغ وصفا للمستثنى بحال متعلقه، فيكون الحال المفرغ عامله،",
     "en": "You may dispense with this strain by making “mufarragh” a qualification of the excepted term by the state of what is connected with it, so that the sense is: [the excepted term] whose governor is emptied;"},
    {"type": "pair",
     "ar": "أو أن تجعل المستثنى مفرغا عن إعرابه للعامل، فيكون المستثنى مفرغا، والعامل مفرغا له.",
     "en": "or by taking the excepted term as emptied of its [own] inflection for the governor, so that the excepted term is “emptied” and the governor is “emptied for it.”"},

    # ---------------- Footnote 8 ----------------
    {"type": "note", "num": "٨"},
    {"type": "pair",
     "ar": "جعل الواو للحال.",
     "en": "He made the wāw circumstantial (ḥāliyya)."},
    {"type": "pair",
     "ar": "ولك أن تجعلها للعطف، وتجعل هو عطفا على المستثنى منه، وفي غير الموجب عطفا على غير المذكور.",
     "en": "You may make it conjunctive, taking “huwa” as coordinated with “the mustathnā minhu” and “in non-affirmative [speech]” as coordinated with “not mentioned.”"},
]
