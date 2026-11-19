# -*- coding: utf-8 -*-
"""Mulla Jami — al-Fawāʾid al-Ḍiyāʾiyya. Source PDF page 474 (printed ٤٧٣)."""

PAGE_NUMBER = 474
PRINTED_PAGE = "٤٧٣"   # Arabic-Indic, as printed

BLOCKS = [
    # ---------------- The commentary text (matn) ----------------
    # Continues «… لانحطاط رتبتهما عن رتبة اسم» at the foot of PDF p. 473.
    {"type": "matn",
     "ar": "الفاعل، فإنه يعمل في مظهر بعده، سواء كان من متعلقات الموصوف أو لم يكن مثل: «زيد ضارب عمرا»،",
     "en": "…active participle, for it governs an explicit noun after it, whether or not that noun is among the connections of the qualified noun, as in “Zayd is striking ʿAmr”."},
    {"type": "matn",
     "ar": "وإنما اشترط أن يكون ذلك المسبب مشتركا مفضلا من وجه مفضلا عليه من وجه آخر بعد اتحادهما بالذات،",
     "en": "It was stipulated that that musabbab be shared, preferred in one respect and surpassed in another, while the two are one in essence,"},
    {"type": "matn",
     "ar": "ليخرج[[١]] عنه مثل قولك: «ما رأيت رجلا أحسن كحل عينه من كحل عين زيد»، فإنهما مختلفان بالذات،",
     "en": "only so that there be excluded from it [a case] like your saying “I have not seen a man the kohl of whose eye is more beautiful than the kohl of Zayd’s eye”, for these two differ in essence;"},
    {"type": "matn",
     "ar": "بخلاف الكحل الملحوظ مطلقا المقيد تارة بهذا، وتارة بذلك، فإنه واحد بالذات، مختلف بالاعتبار،",
     "en": "unlike kohl regarded absolutely, restricted at one time to this and at another to that, for it is one in essence and differs in consideration;"},
    {"type": "matn",
     "ar": "ولئلا[[٢]] يبقى على ما هو الأصل في اسم التفضيل، وهو التغاير بحسب الذات بين المفضل والمفضل عليه؛",
     "en": "and so that it should not remain on what is basic in the elative, namely difference in essence between the one preferred and the one surpassed,"},
    {"type": "matn",
     "ar": "ليسهل[[٣]] إخراجه عن المعنى التفضيلي بالنفي كما سيتضح فائدته،",
     "en": "so that removing it from the comparative meaning by negation becomes easy, as the benefit of this will become clear."},
    {"type": "matn",
     "ar": "وإنما اشترط أن يكون اسم التفضيل منفيا؛ إذ عند كونه منفيا يكون بمعنى الفعل ويعمل عمله،",
     "en": "It was stipulated that the elative be negated only because, when it is negated, it has the meaning of the verb and performs its government."},
    {"type": "matn",
     "ar": "وإنما قلنا: إنه عند كونه منفيا يكون بمعنى الفعل (لأنه) أي: «أحسن» في هذا المثال (بمعنى: «حسن») وكذا كل «أفعل» في المواد الآخر بمعنى: «فعل»،",
     "en": "We said that when it is negated it has the meaning of the verb only (because it), that is, “aḥsan” in this example, (has the meaning of “ḥasuna”) (was beautiful); and likewise every “afʿal” in the other materials has the meaning of “faʿula”."},
    {"type": "matn",
     "ar": "وهذه العبارة تحتمل معنيين:",
     "en": "This expression admits two meanings."},
    {"type": "matn",
     "ar": "أحدهما: أن يكون «أحسن» مثلا بعد النفي بمعنى «حسن»؛ لأنه إذا استولى النفي على اسم التفضيل توجه النفي إلى قيده[[٤]] الذي هو الزيادة،",
     "en": "The first: that “aḥsan”, for example, after negation has the meaning of “ḥasuna”; for when negation governs the elative, the negation is directed at its qualification, which is the excess,"},
    {"type": "matn",
     "ar": "فيفيد أنه ليس حسن كحل عين رجل زائدا على كحل عين زيد،",
     "en": "so it conveys that the beauty of the kohl of a man’s eye does not exceed the kohl of Zayd’s eye;"},
    {"type": "matn",
     "ar": "فيبقى أصل حسن كحل عين رجل مقيسا إلى زيد إما بأن يساويه، أو بأن يكون دونه، والمساواة يأباها مقام المدح[[٥]]،",
     "en": "so the basic beauty of the kohl of a man’s eye remains, measured against Zayd, either by equalling it or by being below it; and equality is refused by the context of praise."},
    {"type": "matn",
     "ar": "فيرجع المعنى إلى أنه حسن في عين كل أحد الكحل دون حسنه في عين زيد، فيكون «أحسن» مع النفي بمعنى: «حسن».",
     "en": "So the meaning comes down to this: kohl is beautiful in everyone’s eye below its beauty in Zayd’s eye; and thus “aḥsan” with negation has the meaning of “ḥasuna”."},

    {"type": "rule"},

    # ---------------- Footnote 1 ----------------
    {"type": "note", "num": "١"},
    {"type": "pair",
     "ar": "مرتبة على الاشتراط المذكور.",
     "en": "Consequent upon the stipulation mentioned."},

    # ---------------- Footnote 2 ----------------
    {"type": "note", "num": "٢"},
    {"type": "pair",
     "ar": "علة باعثة عليه.",
     "en": "A motivating cause for it."},

    # ---------------- Footnote 3 ----------------
    {"type": "note", "num": "٣"},
    {"type": "pair",
     "ar": "متعلق بقوله: لئلا.",
     "en": "Attached to his words “so that … not” (li-allā)."},

    # ---------------- Footnote 4 ----------------
    {"type": "note", "num": "٤"},
    {"type": "pair",
     "ar": "لما ذكره الشيخ عبد القاهر من أن كل كلام فيه قيد زائد على النفي والإثبات يكون ذلك القيد محط الفائدة.",
     "en": "Because of what Shaykh ʿAbd al-Qāhir stated: that in every utterance containing a qualification additional to negation and affirmation, that qualification is the focus of the information conveyed."},

    # ---------------- Footnote 5 ----------------
    {"type": "note", "num": "٥"},
    {"type": "pair",
     "ar": "هذا البيان يخص مثالا يكون المقصود منه المدح وعمل اسم التفضيل المذكور لا يخص بمقام المدح،",
     "en": "This explanation is specific to an example whose purpose is praise, while the government of the elative mentioned is not specific to the context of praise;"},
    {"type": "pair",
     "ar": "فربما يكون النفي نفيا للزيادة مع بقاء إفادة أصل الفعل سواء كان على وجه المساواة أو على وجه يكون دون حسن المفضل في المعنى.",
     "en": "for the negation may be a negation of the excess while the conveying of the basic act remains, whether by way of equality or in such a way that it is below the beauty of what is preferred in meaning."},
    # REVIEW: printed «هو هذا الوجه ذو الثاني» — «ذو» is odd here (perhaps for «دون»); transcribed as printed, translated by sense.
    {"type": "pair",
     "ar": "وعلى هذا عرفت أن المعتمد هو هذا الوجه ذو الثاني لعدم اطراده في تركيب ليس في مقام المدح بخلاف هذا الوجه،",
     "en": "On this basis you know that what is relied upon is this way [of explaining], not the second, since that does not hold consistently in a construction not in the context of praise, unlike this way;"},
    {"type": "pair",
     "ar": "فإن أصل بيانه يجري في الجميع، وألا يجري بعض ما ذكره الشارح، ولا يتوقف عليه أصل البيان، فتأمل.",
     "en": "for the basis of its explanation applies in all [cases], even if part of what the commentator mentioned does not apply, and the basis of the explanation does not depend on it. Reflect."},
]
