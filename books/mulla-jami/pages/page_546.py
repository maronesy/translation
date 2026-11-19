# -*- coding: utf-8 -*-
"""Mulla Jami — al-Fawāʾid al-Ḍiyāʾiyya. Source PDF page 546 (printed ٥٤٥)."""

PAGE_NUMBER = 546
PRINTED_PAGE = "٥٤٥"   # Arabic-Indic, as printed

BLOCKS = [
    {"type": "section", "ar": "[رب]",
     "en": "Rubba"},

    # ---------------- The commentary text (matn) ----------------
    {"type": "matn",
     "ar": "(ورب: للتقليل) أي: لإنشاء التقليل.",
     "en": "(And rubba is for diminution (taqlīl)), that is, for expressing (inshāʾ) diminution."},
    {"type": "matn",
     "ar": "(و) لهذا وجب (لها صدر الكلام) كما أن «كم» وجب لها صدر الكلام، لكونها لإنشاء التكثير.",
     "en": "(And) for this reason (the head of the sentence belongs to it) necessarily, just as the head of the sentence belongs necessarily to “kam”, because it is for expressing multiplication (taktīr)."},
    {"type": "matn",
     "ar": "(مختصة بنكرة) لعدم احتياجها إلى المعرفة[[١]].",
     "en": "(Restricted to an indefinite noun), since it has no need of a definite one,"},
    {"type": "matn",
     "ar": "(موصوفة) ليتحقق التقليل الذي هو مدلول «رب»؛ لأنه إذا وصف الشيء صار أخص وأقل مما لم يوصف.",
     "en": "(qualified [by an adjective]), so that the diminution which is what “rubba” signifies may be realized; for when a thing is qualified it becomes more specific and fewer than what is not qualified."},
    {"type": "matn",
     "ar": "واشتراط[[٢]] كونها موصوفة إنما هو (على) المذهب (الأصح). وهذا مذهب أبي علي ومن وافقه[[٣]].",
     "en": "The requirement that it be qualified holds only (according to the soundest) view. This is the view of Abū ʿAlī and those who agree with him."},
    {"type": "matn",
     "ar": "وقيل[[٤]]: لا يجب ذلك.",
     "en": "It has also been said that this is not necessary."},
    {"type": "matn",
     "ar": "والمختار عند المصنف: الوجوب.",
     "en": "The view chosen by the author is that it is necessary."},
    {"type": "matn",
     "ar": "وهذا الذي ذكره من التقليل أصلها، ثم يستعمل في معنى التكثير[[٥]] كالحقيقة[[٦]]، وفي التقليل كالمجاز المحتاج إلى القرينة.",
     "en": "This diminution that he mentioned is its original [sense]; it then came to be used in the sense of multiplication as though literally, and in diminution as though a figurative usage needing a contextual indicator (qarīna)."},
    {"type": "matn",
     "ar": "(وفعلها) أي: فعل «رب» يعني: الذي تعلق به «رب» فعل (ماض[[٧]])؛ لأنها للتقليل",
     "en": "(And its verb), that is, the verb of “rubba”, meaning the one to which “rubba” attaches, is (a past [verb]); because it is for diminution…"},

    {"type": "rule"},

    # ---------------- Footnote 1 ----------------
    {"type": "note", "num": "١"},
    {"type": "pair",
     "ar": "لا فرق بين «رب» وسائر حروف الجر حتى يمنع عن المعرفة لعدم احتياجها، ولا يمنع غيرها،",
     "en": "There is no difference between “rubba” and the other prepositions such that it should be barred from the definite noun because it has no need of it, while the others are not barred."},
    {"type": "pair",
     "ar": "فالوجه على ما بينه الرضي أنه لا يتحقق التقليل في المعرفة؛ لأنها إما للنكرة، فينافيه، وإما للواحد المعين، فلا يجري فيه التقليل؛ لأنه إنما يجري فيما فيه مظنة الكثرة.",
     "en": "The [correct] reason, as al-Raḍī explained, is that diminution is not realized in a definite noun: for it is either [definite] of an indefinite [genus], which conflicts with it, or of a single specified individual, in which diminution does not apply, since it applies only where multiplicity is to be expected."},
    {"type": "pair",
     "ar": "ولك أن تقول: إن مجرور «رب» في معنى المتميز عنها؛ لأنها للتقليل كما أن «كم» للتكثير، ففيه شائبة العدد الطالب للمتميز،",
     "en": "You may also say that the noun governed by “rubba” is in the sense of the specificand (al-mutamayyiz) of it; for it is for diminution just as “kam” is for multiplication, so there is in it a trace of number, which requires a specificand."},
    {"type": "pair",
     "ar": "وهذا وجه وجيه، وإن خلا عن بيانهم.",
     "en": "This is a sound reason, even if their explanations lack it."},

    # ---------------- Footnote 2 ----------------
    {"type": "note", "num": "٢"},
    {"type": "pair",
     "ar": "إشارة إلى أن قوله: «على الأصح» قيد لقوله: موصوفة لا النكرة أيضا؛ لأن اختصاصها بالنكرة متفق عليه.",
     "en": "An indication that his words “according to the soundest” qualify his word “qualified”, and not “indefinite” as well, since its restriction to the indefinite is agreed upon."},

    # ---------------- Footnote 3 ----------------
    {"type": "note", "num": "٣"},
    {"type": "pair",
     "ar": "أي: المبرد وابن السراج على ما في الرضي.",
     "en": "That is, al-Mubarrad and Ibn al-Sarrāj, according to what is in al-Raḍī."},

    # ---------------- Footnote 4 ----------------
    {"type": "note", "num": "٤"},
    {"type": "pair",
     "ar": "قائله: الأخفش والفراء ومن وافقهما.",
     "en": "Those who held it are al-Akhfash, al-Farrāʾ and those who agree with them."},

    # ---------------- Footnote 5 ----------------
    {"type": "note", "num": "٥"},
    {"type": "pair",
     "ar": "وبقي له اشتراط وصف مدخولها، وإن انتفى عنه موجبه من التقليل.",
     "en": "The requirement that what it enters upon be qualified remained with it, even though its cause, diminution, no longer applies to it."},

    # ---------------- Footnote 6 ----------------
    {"type": "note", "num": "٦"},
    {"type": "pair",
     "ar": "فإن المجاز المشهور يلحق بالحقيقة، والحقيقة المتروكة بالمجاز.",
     "en": "For a well-known figurative usage is classed with literal usage, and an abandoned literal usage with figurative usage."},

    # ---------------- Footnote 7 ----------------
    {"type": "note", "num": "٧"},
    {"type": "pair",
     "ar": "مذهب أكثر النحويين، ومنهم المبرد والفارسي أن ما يتعلق به «رب» يجب أن يكون ماضيا.",
     "en": "The view of most grammarians, among them al-Mubarrad and al-Fārisī, is that what “rubba” attaches to must be past."},
    {"type": "pair",
     "ar": "وذهب ابن السراج إلى أن يكون حالا. ومنع أن يكون مستقبلا.",
     "en": "Ibn al-Sarrāj held that it may be present, and disallowed its being future."},
    {"type": "pair",
     "ar": "وذهب بعض النحويين إلى أنه يجوز أن يكون ماضيا أو حالا أو مستقبلا، والمضي أكثر،",
     "en": "Some grammarians held that it may be past, present or future, the past being more frequent."},
    {"type": "pair",
     "ar": "وهو اختيار ابن مالك وهو الصحيح، كذا في شرح التسهيل.",
     "en": "This is the view chosen by Ibn Mālik, and it is the correct one. So it is in Sharḥ al-Tashīl."},
]
