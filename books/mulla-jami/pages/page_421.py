# -*- coding: utf-8 -*-
"""Mulla Jami — al-Fawāʾid al-Ḍiyāʾiyya. Source PDF page 421 (printed ٤٢٠)."""

PAGE_NUMBER = 421
PRINTED_PAGE = "٤٢٠"   # Arabic-Indic, as printed

BLOCKS = [
    # ---------------- The commentary text (matn) ----------------
    # PDF p. 420 ends with a complete sentence («...فإنه بهذا الاعتبار نكرة.»); this page opens a new item.
    {"type": "matn",
     "ar": "(و) الثالث: (المبهمات) يعني: أسماء الإشارات والموصولات[[١]]، وإنما سميت مبهمات؛ لأن اسم الإشارة من غير إشارة مبهم، وكذا الموصول من غير صلة،",
     "en": "(And) the third: (the vague nouns (mubhamāt)), meaning demonstrative nouns (asmāʾ al-ishāra) and relative nouns (mawṣūlāt). They are called “vague” only because a demonstrative noun without an act of pointing is vague, and likewise a relative noun without a relative clause (ṣila)."},
    {"type": "matn",
     "ar": "وهذا القسم من قبيل الوضع العام والموضوع له الخاص، فإنها موضوعة بإزاء معان متعينة معلومة معهودة من حيث معلوميتها ومعهوديتها وضعا عاما كليا،",
     "en": "This class belongs to the type in which the imposition (waḍʿ) is general and the thing for which [the word] is imposed (al-mawḍūʿ lahu) is particular: they are imposed for determinate meanings, known and familiar, insofar as they are known and familiar, by a general, universal imposition."},
    {"type": "matn",
     "ar": "فإن الواضع إذا تعقل مثلا معنى المشار إليه المفرد المذكور، وعين لفظا بإزاء كل واحد من أفراد هذا المفهوم كان هذا وضعا عاما؛",
     "en": "For if the imposer of language (al-wāḍiʿ) conceives, for example, the meaning “a singular masculine thing pointed to” and assigns an expression to each one of the individuals of this concept, this is a general imposition,"},
    {"type": "matn",
     "ar": "لأن التصور المعتبر فيه عام -وهو المشترك بين تلك الأفراد- والموضوع له خاص؛ لأن خصوصية كل واحد من تلك الأفراد، لا المفهوم المشترك بينها.",
     "en": "because the conception taken into account in it is general—namely what is common to those individuals—while the thing for which it is imposed is particular, because it is the particularity of each one of those individuals, not the concept common to them."},
    {"type": "matn",
     "ar": "(و) الرابع والخامس: (ما عرف باللام) العهدية أو الجنسية أو الاستغراقية[[٢]].",
     "en": "(And) the fourth and the fifth: (what is made definite by the lām), whether of prior reference (ʿahdiyya), of the genus (jinsiyya) or of all-inclusiveness (istighrāqiyya)."},
    {"type": "matn",
     "ar": "وإنما لم يقل: «ما دخله اللام» لئلا يدخل فيه ما دخله اللام الزائدة[[٣]] لتحسين اللفظ،",
     "en": "He did not say “what the lām has entered” only so that there would not be included in it what the redundant lām, added to embellish the wording, has entered,"},
    {"type": "matn",
     "ar": "والميم في: «ليس من امبر امصيام في امسفر» بدل من اللام[[٤]]، فلا يعد ما دخلته قسما آخر من المعارف",
     "en": "and the mīm in “laysa min am-birri am-ṣiyāmu fī am-safari” (it is not righteousness to fast while travelling) is a substitute for the lām; so what it enters is not counted as another class of definite nouns."},
    {"type": "matn",
     "ar": "(أو) عرف (بالنداء) نحو: «يا رجل»[[٥]] إذا قصد به معين، بخلاف «يا رجلا» لغير معين، فإنه نكرة،",
     "en": "(Or) [what is] made definite (by the vocative), as in “yā rajulu” (O man!) when a specific person is meant by it, unlike “yā rajulan” for a non-specific one, for that is indefinite."},
    {"type": "matn",
     "ar": "ولم يذكره المتقدمون؛ لرجوعه إلى ذي اللام[[٦]]؛ إذ",
     "en": "The earlier [grammarians] did not mention it, because it reduces to the noun with the lām, since…"},

    {"type": "rule"},

    # ---------------- Footnote 1 ----------------
    {"type": "note", "num": "١"},
    {"type": "pair",
     "ar": "لعل وجه كون الموصول في مرتبة اسم الإشارة اشتراكهما في الإبهام والتعين بأمر خارج، أعني: الإشارة والصلة،",
     "en": "Perhaps the reason the relative noun is of the same rank as the demonstrative noun is that both share vagueness and determination by something external, namely the pointing and the relative clause;"},
    {"type": "pair",
     "ar": "وتفاوتهما وضوحا بحسب تفاوت الإشارة والصلة في الوضوح غير معتد به.",
     "en": "their difference in clarity, according to the difference in clarity between the pointing and the relative clause, is not taken into account."},
    {"type": "pair",
     "ar": "وذهب الأخفش إلى أن ما فيه ال من الموصولات تعرف بها، وما ليست فيه ال ك«من وما»، فتعرفه لأنه في معنى ما فيه ال، فالموصول على هذا في مرتبة ذي اللام.",
     "en": "Al-Akhfash held that the relative nouns containing al are made definite by it, while those without al, like “man” and “mā”, are definite because they have the meaning of what contains al; on this view the relative noun is of the rank of the noun with the lām."},
    {"type": "pair",
     "ar": "وإليه ذهب سيبويه وجمهور النحاة.",
     "en": "Sībawayh and the majority of the grammarians held this view."},

    # ---------------- Footnote 2 ----------------
    {"type": "note", "num": "٢"},
    {"type": "pair",
     "ar": "فيه أن اللام منحصرة في اللام العهدية الجنسية والاستغراقية والعهدية الذهنية من فروع الجنسية، كما حقق في أول الكتاب،",
     "en": "Against this: the lām is confined to the lām of prior reference, the generic lām and the lām of all-inclusiveness, and the lām of mental reference (al-ʿahdiyya al-dhihniyya) is a branch of the generic, as was established at the beginning of the book;"},
    {"type": "pair",
     "ar": "فتقسيمها إلى الجنسية والاستغراقية تقسيم الشيء إلى نفس الشيء، وتقسيمه، وكذا إلى العهدية والجنسية في وجه.",
     "en": "so dividing it into the generic and the all-inclusive is dividing a thing into the thing itself and its division, and so too [dividing it] into the lām of prior reference and the generic, in one respect."},

    # ---------------- Footnote 3 ----------------
    {"type": "note", "num": "٣"},
    {"type": "pair",
     "ar": "هي فيما وجب تعريفه أو تنكيره في التسهيل.",
     "en": "It is [found] in what must be definite or must be indefinite, according to al-Tashīl."},
    {"type": "pair",
     "ar": "وقد تعرض زيادتها في علم وحال وتمييز لا غير ومضاف.",
     "en": "Its redundancy may occur in a proper name, a circumstantial accusative (ḥāl) and a specificative (tamyīz), and nothing else, and in a governing noun of a genitive construction (muḍāf)."},

    # ---------------- Footnote 4 ----------------
    {"type": "note", "num": "٤"},
    {"type": "pair",
     "ar": "فحينئذ سقط ما ذكره في قوله: من خواصه دخول اللام أنه لو قال: دخول حرف التعريف لكان شاملا للميم إلا أنه لم يذكر الميم لعدم شهرته؛",
     "en": "Accordingly, what was said about his words “among its properties is the entry of the lām” falls away—namely that, had he said “the entry of the particle of definiteness”, it would have included the mīm, except that he did not mention the mīm because it is not well known;"},
    {"type": "pair",
     "ar": "لأنه إذا لم يكن حرف تعريف، بل بدلا منه، فلا يشمله حرف التعريف أيضا، كما لا يشمل الحروف المبدلة من اللام في قولك: الرحمن والصمد والرحيم إلى غير ذلك.",
     "en": "for if it is not a particle of definiteness but a substitute for one, “particle of definiteness” does not cover it either, just as it does not cover the letters substituted for the lām in your saying al-Raḥmān, al-Ṣamad, al-Raḥīm and the like."},

    # ---------------- Footnote 5 ----------------
    {"type": "note", "num": "٥"},
    {"type": "pair",
     "ar": "أي: اسم الجنس الذي قصد به فرد معين، فإن تعريفه بالنداء.",
     "en": "That is, a generic noun by which a specific individual is meant, for its definiteness is through the vocative."},
    {"type": "pair",
     "ar": "وأما العلم المنادى فتعريفه بالعلمية والنداء، أفاد زيادة الوضوح وهو المختار.",
     "en": "As for the proper name in the vocative, its definiteness is through being a proper name, and the vocative adds further clarity; this is the preferred view."},
    {"type": "pair",
     "ar": "وقيل: إنه عرف بالنداء بعد إزالة العلمية.",
     "en": "It has also been said that it is made definite by the vocative after its status as a proper name is removed."},

    # ---------------- Footnote 6 ----------------
    {"type": "note", "num": "٦"},
    {"type": "pair",
     "ar": "وهو مذكور في المتون، وكأنه لم يكن في متنه أو هناك سهو كاتب،",
     "en": "It is mentioned in the base texts; it seems it was not in his copy of the text, or there is a scribal slip there."},
    {"type": "pair",
     "ar": "وكان أصله ولم يذكره المتقدمون لرجوعه إلى ذي اللام على ما في الهندي،",
     "en": "Its original wording was “and the earlier [grammarians] did not mention it, because it reduces to the noun with the lām”, according to what is in al-Hindī."},
    {"type": "pair",
     "ar": "ووجه كونه في الأصل يا أيها الرجل خفي، فالأظهر ما في الرضي،",
     "en": "The reason for its being originally “yā ayyuhā l-rajulu” is obscure; what is in al-Raḍī is more evident."},
    {"type": "pair",
     "ar": "ومن لم يعده من النحويين، فلكونه فرع المضمرات؛ لأن تعرفه لوقوعه موقع كاف الخطاب.",
     "en": "Those grammarians who did not count it [separately] did so because it is a branch of the pronouns, since its definiteness is due to its occupying the place of the kāf of address."},
]
