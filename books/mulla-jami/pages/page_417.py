# -*- coding: utf-8 -*-
"""Mulla Jami — al-Fawāʾid al-Ḍiyāʾiyya. Source PDF page 417 (printed ٤١٦)."""

PAGE_NUMBER = 417
PRINTED_PAGE = "٤١٦"   # Arabic-Indic, as printed

BLOCKS = [
    # ---------------- The commentary text (matn) ----------------
    # Continues «والفرق أنه يقال: «المال عند زيد» فيما يحضر عنده» from PDF p. 416.
    {"type": "matn",
     "ar": "وفيما في خزائنه؛ وإن كان غائبا عنه، ولا يقال: «المال لدى زيد، أو لدن زيد»، إلا فيما يحضر عنده.",
     "en": "…and of what is in his storehouses, even if it is absent from him; but one does not say “al-mālu ladā zaydin” or “ladun zaydin” except of what is present with him."},
    {"type": "matn",
     "ar": "وحكمها أن يجر بها[[١]] على الإضافة نحو: «المال لدى زيد»،",
     "en": "Their rule is that [the noun after them] is put in the genitive by them through annexation, as in “al-mālu ladā zaydin”."},
    {"type": "matn",
     "ar": "وقد ينصب في بعض لغات العرب بـ«لدن» خاصة «غدوة» سماعا تشبيها لنونها بنون التنوين في مثل: «رطل زيتا»،",
     "en": "In some dialects of the Arabs “ghudwatan” (early morning) is put in the accusative after “ladun” in particular, by attested usage, its nūn being likened to the nūn of tanwīn in such a phrase as “raṭlun zaytan” (a pound of oil);"},
    {"type": "matn",
     "ar": "ولذلك[[٢]] يحذف عنها ويثبت[[٣]]، ولكون[[٤]] «غدوة» أكثر استعمالا من «سحرة»[[٥]] وغيرها.",
     "en": "for this reason it is dropped from it and retained; and because “ghudwa” is used more often than “suḥra” (the last part of the night before dawn) and others."},
    {"type": "matn",
     "ar": "(ومنها: «قط») مفتوح القاف، ومضموم الطاء المشددة، وهذه أشهر لغاته،",
     "en": "(And among them is “qaṭṭu”), with fatḥa on the qāf and ḍamma on the doubled ṭāʾ; this is the best known of its forms."},
    {"type": "matn",
     "ar": "وقد يخفف الطاء المضمومة، وقد يضم القاف اتباعا لضمة الطاء المشددة أو المخففة،",
     "en": "The ṭāʾ with ḍamma is sometimes lightened, and the qāf is sometimes given ḍamma to harmonize with the ḍamma of the ṭāʾ, doubled or lightened;"},
    {"type": "matn",
     "ar": "وقد جاء «قط» ساكنة الطاء مثل: «قط» الذي هو اسم فعل، فهذه خمس لغات",
     "en": "and “qaṭ” has also come with sukūn on the ṭāʾ, like the “qaṭ” that is a verbal noun. These are five forms,"},
    {"type": "matn",
     "ar": "كلها (للماضي المنفي) أي: لأجل الفعل[[٦]] الماضي المنفي، أو الزمان الماضي المنفي وقوع شيء فيه؛",
     "en": "all of them (for the negated past), that is, for the sake of the negated past verb, or the past time in which the occurrence of something is negated,"},
    {"type": "matn",
     "ar": "ليستغرق النفي جميع الأزمنة الماضية نحو: «ما رأيته قط»،",
     "en": "so that the negation takes in all past times, as in “mā raʾaytuhu qaṭṭu” (I have never seen him)."},
    {"type": "matn",
     "ar": "وبناء المخففة[[٧]] لوضعه وضع الحروف، وبناء المشددة لمشابهتها لأختها المخففة، وقيل: حمل على أخته «عوض».",
     "en": "The lightened form is indeclinable because it has the coinage of particles, and the doubled form because it resembles its lightened sister; and it has been said: it is assimilated to its sister “ʿawḍu”."},
    {"type": "matn",
     "ar": "(ومنها: «عوض») بفتح العين، وضم الضاد، وقد جاء فتح الضاد وكسرها",
     "en": "(And among them is “ʿawḍu”), with fatḥa on the ʿayn and ḍamma on the ḍād; fatḥa and kasra on the ḍād have also come."},
    {"type": "matn",
     "ar": "(للمستقبل) أي: لأجل الفعل المستقبل (المنفي) أو الزمان المستقبل المنفي فيه وقوع شيء",
     "en": "(For the negated future), that is, for the sake of the negated future verb, or the future time in which the occurrence of something is negated,"},
    {"type": "matn",
     "ar": "ليستغرق النفي جميع الأزمنة المستقبلة نحو: «لا أراه عوض»، وبناء «عوض»",
     "en": "so that the negation takes in all future times, as in “lā arāhu ʿawḍu” (I will never see him). “ʿAwḍu” is indeclinable…"},

    {"type": "rule"},

    # ---------------- Footnote 1 ----------------
    {"type": "note", "num": "١"},
    {"type": "pair",
     "ar": "إما لفظا إن كان مفردا أو تقديرا إن كان جملة.",
     "en": "Either in form, if it is a single word, or by supposition, if it is a sentence."},

    # ---------------- Footnote 2 ----------------
    {"type": "note", "num": "٢"},
    # REVIEW: «بحذف» printed so (parallel «ويثبت» suggests يحذف); transcribed as printed.
    {"type": "pair",
     "ar": "أي: لكون نونه مشبها بالتنوين بحذف «من لدن» تارة، ويثبت أخرى.",
     "en": "That is, because its nūn is likened to tanwīn, it is dropped from “ladun” at one time and retained at another."},

    # ---------------- Footnote 3 ----------------
    {"type": "note", "num": "٣"},
    {"type": "pair",
     "ar": "هذا إذا كان نصب غدوة قبل الحذف.",
     "en": "This is if the accusative of “ghudwa” comes before the dropping."},
    {"type": "pair",
     "ar": "أما إذا كان الحذف قبله فيقال: شبه نونها بنون التنوين؛ لأنها تثبت تارة، وتحذف تارة.",
     "en": "If the dropping comes before it, one says: its nūn was likened to the nūn of tanwīn because it is retained at one time and dropped at another."},

    # ---------------- Footnote 4 ----------------
    {"type": "note", "num": "٤"},
    {"type": "pair",
     "ar": "عطف على تشبيها من حيث المعنى علة لنصب خصوص غدوة.",
     "en": "It is coordinated in meaning with “tashbīhan” (by likening), as the reason why “ghudwa” in particular is put in the accusative."},

    # ---------------- Footnote 5 ----------------
    {"type": "note", "num": "٥"},
    {"type": "pair",
     "ar": "بضم السين وسكون الحاء السحر الأعلى، والسحر قبيل الصبح، كذا في القاموس.",
     "en": "With ḍamma on the sīn and sukūn on the ḥāʾ: the earliest part of saḥar; and saḥar is the time shortly before dawn. So in al-Qāmūs."},

    # ---------------- Footnote 6 ----------------
    {"type": "note", "num": "٦"},
    {"type": "pair",
     "ar": "في هذا التوجيه صرف اللام عن المتبادر، وهو كونه صلة الوضع، كما مر في أمثاله وإبقاء الماضي المنفي على معناه المتبادر،",
     "en": "This interpretation turns the lām away from its obvious sense, which is its being the complement of the coinage, as has passed in similar cases, and keeps “the negated past” in its obvious sense;"},
    {"type": "pair",
     "ar": "فهو أقل تصرفا مما في التوجيه الثاني إبقاء اللام على المتبادر، وجعل الماضي صفة الزمان، وإسناد المنفي إليه على التجوز باعتبار كون ما وقع فيه منفيا،",
     "en": "so it involves less alteration than the second interpretation, which keeps the lām in its obvious sense, makes “past” a qualifier of time, and attributes “negated” to it figuratively, in view of what occurs in it being negated."},
    {"type": "pair",
     "ar": "وربما استعمل «قط» في النفي.",
     "en": "“Qaṭṭu” is often used in negation."},
    {"type": "pair",
     "ar": "وقد استعمل بدونه لفظا ومعنى نحو: «كنت أراه قط» أي: دائما.",
     "en": "It has been used without it in both form and meaning, as in “kuntu arāhu qaṭṭu”, that is, always."},
    {"type": "pair",
     "ar": "وقد استعمل بدونه لفظا لا معنى نحو: «هل رأيت الذئب قط».",
     "en": "It has been used without it in form but not in meaning, as in “hal raʾayta l-dhiʾba qaṭṭu” (have you ever seen the wolf?)."},

    # ---------------- Footnote 7 ----------------
    {"type": "note", "num": "٧"},
    # REVIEW: «الاستغراقية» is printed with a hamza-like mark over the tooth after the sīn («الاسئغراقية»); transcribed as الاستغراقية.
    {"type": "pair",
     "ar": "وقيل: لتضمنه معنى «في». ومعنى «من» الاستغراقية على سبيل اللزوم.",
     "en": "It has been said: because it includes the meaning of “fī”, and the meaning of the all-inclusive “min” by way of entailment."},
]
