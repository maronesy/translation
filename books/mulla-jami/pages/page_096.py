# -*- coding: utf-8 -*-
"""Mulla Jami — al-Fawāʾid al-Ḍiyāʾiyya. Source PDF page 96 (printed ٩٥)."""

PAGE_NUMBER = 96
PRINTED_PAGE = "٩٥"   # Arabic-Indic, as printed

BLOCKS = [
    # ---------------- The base text (matn) ----------------
    {"type": "matn",
     "ar": "لاعتبارها فيما وضعا له.",
     "en": "because of taking it into account in that for which the two were coined."},
    {"type": "matn",
     "ar": "(وأخر) جمع «أخرى» مؤنث «آخر»، وآخر اسم التفضيل؛ لأن معناه في الأصل: أشد تأخرا، ثم نقل إلى معنى «غير».",
     "en": "(And “ukhar”) is the plural of “ukhrā,” the feminine of “ākhar”; and “ākhar” is an elative (ism al-tafḍīl), because its original meaning is “more delayed,” then it was transferred to the meaning of “ghayr” (other)."},
    {"type": "matn",
     "ar": "وقياس اسم التفضيل أن يستعمل باللام، أو الإضافة، أو بكلمة «من»، وحيث لم يستعمل بواحد منها علم أنه معدول من أحدها.",
     "en": "The rule for the elative is that it be used with the definite article (lām), or with a genitive construction (iḍāfa), or with the word “min”; and since it is used with none of these, it is known that it is deviated from one of them."},
    {"type": "matn",
     "ar": "فقال بعضهم: إنه معدول عما فيه اللام[[١]]، أي: عن الآخر.",
     "en": "Some said: it is deviated from that which contains the lām, that is: from “al-ākhar” (the other)."},
    {"type": "matn",
     "ar": "وقال بعضهم: إنه معدول عما ذكر معه «من» أي: عن آخر من.",
     "en": "Others said: it is deviated from that with which “min” is mentioned, that is: from “ākhar min” (another than)."},
    {"type": "matn",
     "ar": "وإنما لم يذهب أحد إلى تقدير الإضافة[[٢]]؛ لأنها توجب[[٣]] التنوين، أو البناء، أو إضافة أخرى مثلها[[٤]]، نحو: «حينئذ» و«قبل» و:",
     "en": "No one held [it to be deviated from] a presumed genitive construction, because that would necessitate nunation (tanwīn), or indeclinability (bināʾ), or another genitive construction like it — as in “ḥīnaʾidhin,” “qablu,” and:"},
    {"type": "verse",
     "ar": "يا تيم تيم عدي ....",
     "en": "“O Taym, Taym of ʿAdī …”"},
    {"type": "matn",
     "ar": "وليس في «أخر» شيء من ذلك، فتعين أن يكون معدولا عن أحد الآخرين[[٥]].",
     "en": "But in “ukhar” there is nothing of that, so it is determined that it is deviated from one of the two [prior] forms."},
    {"type": "matn",
     "ar": "(وجمع) جمع «جمعاء» مؤنث «أجمع»، وكذلك «كتع وبتع وبصع»، وقياس «فعلاء",
     "en": "(And “jumaʿ”) is the plural of “jamʿāʾ,” the feminine of “ajmaʿ,” and likewise “kutaʿ, butaʿ, and buṣaʿ”; and the analogical rule for “faʿlāʾ”"},

    {"type": "rule"},

    # ---------------- Footnote 1 ----------------
    {"type": "note", "num": "١"},
    {"type": "pair",
     "ar": "يؤيده لزوم المطابقة للموصوف إفرادا وتثنية وجمعا وتذكيرا وتأنيثا، كما هو شأن المستعمل باللام.",
     "en": "It is supported by the obligatory agreement with the qualified noun in singularity, duality, plurality, masculinity, and femininity — as is the case with what is used with the lām."},
    {"type": "pair",
     "ar": "قيل: لكن يدفعه لزوم تخالف المعدول والمعدول عنه تنكيرا وتعريفا؟",
     "en": "It is said: but this is refuted by the obligatory divergence between the deviated form and that from which it deviated in definiteness and indefiniteness."},
    {"type": "pair",
     "ar": "وأجيب عنه: بجواز عدول الاسم لفظا ومعنى، كما في سحر إذا أردت به سحرا بعينه، وهو سحر ليلتك، فإنه معدول عن السحر لفظا ومعنى.",
     "en": "The reply to it is: that a noun may deviate in both wording and meaning, as in “saḥar” when you intend by it a particular daybreak — namely the daybreak of your [own] night — for it is deviated from “al-saḥar” in both wording and meaning."},
    {"type": "pair",
     "ar": "أما لفظا: فلأن كل جنس أطلق وأريد به فرد معين من أفراده، فلا بد من لام العهد سواء صار بالغلبة علما، نحو: النجم أو لا نحو: ﴿فعصى فرعون الرسول فأخذناه أخذا وبيلا﴾ (سورة المزمل:١٦).",
     "en": "As for wording: because whenever a generic term is used unrestrictedly and yet a specific individual of its instances is intended, the article of [definite] reference (lām al-ʿahd) is indispensable — whether it has become a proper name by predominance, as in “al-Najm,” or not, as in: “So Pharaoh disobeyed the Messenger, and We seized him with a ruinous seizing” (Qurʾān, Sūrat al-Muzzammil 73:16)."},
    {"type": "pair",
     "ar": "وأما معنى: فلأنه لو كان معنى اللام محفوظا لبني لتضمنه معنى الحرف مع أنه معرب وغير منصرف في المشهور.",
     "en": "As for meaning: because if the sense of the lām were preserved, [the word] would be indeclinable through its implying the meaning of a particle — yet it is declinable and diptote (denied full inflection) on the well-known view."},
    {"type": "pair",
     "ar": "وذلك بالعدل والعلمية المقدرة كأمس حالة الرفع عند بني تميم، فإنه المعدول عن الأمس، وغير منصرف بالعلمية المقدرة والعدل.",
     "en": "And that is by deviation and presumed proper-name status, like “ams” (yesterday) in the nominative case according to Banū Tamīm, for it is deviated from “al-ams” and is diptote by [its] presumed proper-name status and deviation."},
    {"type": "pair",
     "ar": "وأما حالتي النصب والجر فمبني عندهم، وكضحى إذا أردت به ضحى يومك عند الجوهري.",
     "en": "As for the accusative and genitive cases, it is indeclinable in their [usage]; and [it is] like “ḍuḥā” (forenoon) when you intend by it the forenoon of your [own] day, according to al-Jawharī."},
    {"type": "pair",
     "ar": "والقياس يقتضي أن يكون صباح ومساء معينين كأمس وسحر مع أنهما منصرفان اتفاقا.",
     "en": "Analogy would require that “ṣabāḥ” and “masāʾ,” when made specific, be like “ams” and “saḥar” — yet the two are fully inflected by consensus."},

    # ---------------- Footnote 2 ----------------
    {"type": "note", "num": "٢"},
    {"type": "pair",
     "ar": "أي: فرضها واعتبارها.",
     "en": "That is: supposing it and taking it into account."},

    # ---------------- Footnote 3 ----------------
    {"type": "note", "num": "٣"},
    {"type": "pair",
     "ar": "الحصر ممنوع بما ذهب إليه الخليل في أجمع وأخواته، فالأولى أن يقال: إن المضاف إليه لا يحذف إلا إذا جاز إظهاره، ولا يجوز إظهاره ههنا.",
     "en": "The [claimed] exclusivity is disproved by what al-Khalīl held concerning “ajmaʿ” and its sisters; so it is preferable to say: the term to which [a noun] is annexed is not elided except when its explicit mention is permissible — and its explicit mention is not permissible here."},

    # ---------------- Footnote 4 ----------------
    {"type": "note", "num": "٤"},
    {"type": "pair",
     "ar": "في المضاف إليه سواء كان المضاف الثاني تكرارا للأول أو لا، نعم يشترط أن يكون تابعا للأول.",
     "en": "[This is] with respect to the term annexed to, whether the second annexed [term] is a repetition of the first or not; yes, it is stipulated that it be a follower (tābiʿ) of the first."},
    {"type": "pair",
     "ar": "ولذا قال الشيخ الرضي: بدل تلك العبارة: أو دلالة ما أضيف إليه تابع ذلك المضاف إليه نحو: إلا علالة أو بداهة سابح.",
     "en": "For this reason al-Shaykh al-Raḍī said, in place of that expression: “or the indication of that which is annexed to [it], being a follower of that annexed term,” as in: “illā ʿilālata aw badāhata sābiḥin.”"},

    # ---------------- Footnote 5 ----------------
    {"type": "note", "num": "٥"},
    {"type": "pair",
     "ar": "يجوز فيه ضم الهمزة وفتحها.",
     "en": "Both the ḍamma and the fatḥa are permissible on its hamza [i.e., al-ākharīn / al-ākharayn]."},
]
