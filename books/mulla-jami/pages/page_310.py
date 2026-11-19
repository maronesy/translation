# -*- coding: utf-8 -*-
"""Mulla Jami — al-Fawāʾid al-Ḍiyāʾiyya. Source PDF page 310 (printed ٣٠٩)."""

PAGE_NUMBER = 310
PRINTED_PAGE = "٣٠٩"   # Arabic-Indic, as printed

BLOCKS = [
    # ---------------- The commentary text (matn) ----------------
    # Follows «فعلى البدل دون الإضافة.» at the foot of PDF p. 309 (new sentence).
    {"type": "matn",
     "ar": "(و) الإضافة (اللفظية) علامتها: (أن يكون) المضاف (صفة) احتراز عما إذا لم يكن صفة نحو: «غلام زيد»",
     "en": "(And) the (formal [lafẓiyya]) genitive construction: its mark is (that) the annexed term (be an adjective [ṣifa]), as a precaution against the case where it is not an adjective, as in “ghulām Zayd” (Zayd’s slave),"},
    {"type": "matn",
     "ar": "(مضافة إلى معمولها[[١]]) احتراز عما إذا كانت مضافة إلى غير معمولها، نحو: «مصارع البلد، وكريم العصر»[[٢]]",
     "en": "(annexed to what it governs [maʿmūl]), as a precaution against the case where it is annexed to what it does not govern, as in “muṣāriʿ al-balad” (the wrestler of the town) and “karīm al-ʿaṣr” (the noble man of the age);"},
    {"type": "matn",
     "ar": "(مثل: «ضارب زيد») من قبيل إضافة اسم الفاعل إلى مفعوله (و«حسن الوجه») من قبيل إضافة الصفة المشبهة إلى فاعلها.",
     "en": "(as in “ḍārib Zayd” [the one beating Zayd]), of the type of an active participle annexed to its object, (and “ḥasan al-wajh” [fair of face]), of the type of the resembling adjective (al-ṣifa al-mushabbaha) annexed to its agent."},
    {"type": "matn",
     "ar": "(ولا تفيد) الإضافة اللفظية فائدة (إلا تخفيفا) لا تعريفا ولا تخصيصا[[٣]] لكونها في تقدير الانفصال",
     "en": "(And) the formal genitive construction (conveys) no benefit (except lightening [takhfīf]), neither definiteness nor specification, because it is in the sense of separation,"},
    {"type": "matn",
     "ar": "(في اللفظ[[٤]]) لا في المعنى[[٥]] بأن يسقط بعض المعاني عن ملاحظة",
     "en": "(in the wording), not in the meaning, in that some meanings drop from consideration…"},

    {"type": "rule"},

    # ---------------- Footnote 1 ----------------
    {"type": "note", "num": "١"},
    {"type": "pair",
     "ar": "قال الشيخ الرضي: ما حاصله: أن الصفة المشبهة جائزة العمل أبدا فيما هو فاعلها، وإضافتها إليه لفظية،",
     "en": "Shaykh al-Raḍī said, in substance: the resembling adjective may always govern what is its agent, and its annexation to it is formal;"},
    {"type": "pair",
     "ar": "وإن اسمي الفاعل والمفعول يعملان في المرفوع، والظرف والمصدر سواء كانا بمعنى الماضي أو الحال أو الاستقبال أو الاستمرار،",
     "en": "and the active and passive participles govern the nominative, the adverbial (ẓarf) and the maṣdar, whether they bear the sense of the past, the present, the future or continuity;"},
    {"type": "pair",
     "ar": "ويضافان إلى مرفوع هو سبب، نحو: «زيد ضامر بطنه، ومؤدب خدامه» لا إلى مرفوع لم يكن سببا، نحو: «مررت برجل قائم في داره عمرو، ومضروب على بابه بكر».",
     "en": "and they are annexed to a nominative that is causally connected [to the qualified noun] (sababī), as in “Zayd is lean of belly” and “… whose servants are disciplined,” but not to a nominative that is not so connected, as in “I passed by a man in whose house ʿAmr is standing, and at whose door Bakr is beaten.”"},
    {"type": "pair",
     "ar": "ويعملان في غير ما ذكر من المفعول به وغيره إذا كانا بمعنى الحال أو الاستقبال أو الاستمرار،",
     "en": "They govern what was not mentioned, the direct object and others, when they bear the sense of the present, the future or continuity;"},
    {"type": "pair",
     "ar": "وإضافتهما إلى المفعول به والمفعول فيه لفظية على الأولين، وعلى الثالث يحتملها والمعنوية.",
     "en": "and their annexation to the direct object and the adverbial object (mafʿūl fīh) is formal on the first two [senses], while on the third it admits both it and the semantic [annexation]."},
    {"type": "pair",
     "ar": "وقد يؤول بعض الأسماء باسم الفاعل والمفعول المستمر، فتصير الإضافة لفظية كما يؤول القيد بالمقيد، والعير بكسر العين أو ضمها وسكون الباء الموحدة بالعائر.",
     "en": "Some nouns are interpreted as a continuous active or passive participle, so the annexation becomes formal; as “al-qayd” is interpreted as “al-muqayyid” (the one that fetters), and “al-ʿīr,” with kasra or ḍamma on the ʿayn and sukūn on the one-dotted bāʾ, as “al-ʿāʾir.”"},
    # REVIEW: the gloss describes «العير» as having a «باء موحدة» with sukūn, but the word as printed has a yāʾ, not a bāʾ; transcribed as printed.

    # ---------------- Footnote 2 ----------------
    {"type": "note", "num": "٢"},
    {"type": "pair",
     "ar": "فإن قلت: البلد مفعول فيه لـ«مصارع»، وكذا العصر مفعول فيه لـ«كريم»؟",
     "en": "If you say: “al-balad” is an adverbial object of “muṣāriʿ,” and likewise “al-ʿaṣr” is an adverbial object of “karīm”?"},
    {"type": "pair",
     "ar": "قلت: لا يعمل اسم الفاعل بدون الاعتماد، فليكن المراد مصارع للبلد وكريم للعصر فيما لم يعتمد",
     "en": "I say: the active participle does not govern without support (iʿtimād); so let what is meant be “a wrestler belonging to the town” and “a noble man belonging to the age,” where there is no support;"},
    {"type": "pair",
     "ar": "أو أيضا شرط وجوب عمل اسم الفاعل أن يكون بمعنى الحال أو الاستقبال، وإذا كان بمعنى الاستمرار فعمله جائز، فليكن المثالان بمعنى الماضي أو الاستمرار.",
     "en": "or also: the condition for the active participle’s necessarily governing is that it bear the sense of the present or the future, and when it bears the sense of continuity its governing is permissible; so let the two examples bear the sense of the past or of continuity."},
    {"type": "pair",
     "ar": "وقد يقال: إضافة الصفة إلى المعمول دائرة على اعتبار المتكلم،",
     "en": "It is also said: the annexation of an adjective to what it governs turns on the speaker’s consideration;"},
    {"type": "pair",
     "ar": "فإن قصد تعلق العامل بالمعمول وإضافته فلفظية، وإن قصد تقدير حرف جر من حروف معتبرة في الإضافة فمعنوية.",
     "en": "if he intends the governor’s attachment to what it governs and its annexation [to it], it is formal; and if he intends an implied preposition from among those taken into account in annexation, it is semantic."},
    {"type": "pair",
     "ar": "قيل: اسم الفاعل والمفعول يعملان في المرفوع والمنصوب بالظرفية والمصدرية من غير اشتراط زمان.",
     "en": "It has been said: the active and passive participles govern the nominative, and the accusative as an adverbial and as a maṣdar, without any condition of time;"},
    {"type": "pair",
     "ar": "وإنما اشترط الزمان للعمل في المفعول به وغيره مما لم يذكر سابقا، وهذا خلاف ما سيأتي في المتن.",
     "en": "time is a condition only for governing the direct object and whatever else was not mentioned earlier; and this is contrary to what will come in the base text."},
    {"type": "pair",
     "ar": "وقيل: إضافة اسم الفاعل أو اسم المفعول إنما هي إلى المرفوع السببي لا غير، فيقال: «زيد ضامر بطنه، ومؤدب خدامه» لا إلى غيره كما في «زيد ضارب في داره عمرو».",
     "en": "It has also been said: the annexation of the active or the passive participle is only to the causally connected nominative and nothing else; so one says “Zayd is lean of belly” and “… whose servants are disciplined,” but not to another, as in “Zayd, in whose house ʿAmr is beating.”"},

    # ---------------- Footnote 3 ----------------
    {"type": "note", "num": "٣"},
    {"type": "pair",
     "ar": "اعلم أنه يجوز إنما تفيد تخفيفا لا تعريفا ولا تخصيصا، ولا يجوز لا تفيد إلا تخفيفا لا تعريفا ولا تخصيصا،",
     "en": "Know that it is permissible to say “it conveys only lightening, not definiteness or specification,” but not permissible to say “it conveys nothing but lightening, not definiteness or specification”;"},
    {"type": "pair",
     "ar": "فالأولى أن يقول: أي: تفيد تخفيفا في اللفظ لا تعريفا ولا تخصيصا.",
     "en": "so it would have been better for him to say: that is, “it conveys lightening in the wording, not definiteness or specification.”"},

    # ---------------- Footnote 4 ----------------
    {"type": "note", "num": "٤"},
    {"type": "pair",
     "ar": "أي: إلا خفة في اللفظ، صرح بقوله: «في اللفظ» للإشارة إلى وجه التسمية، أو للتصريح بالمقابلة، أو للاحتراز عن خفة في المعنى، كما أشار إليه قدس سره.",
     "en": "That is, “except lightness in the wording.” He stated “in the wording” explicitly to indicate the reason for the name [lafẓiyya], or to state the contrast explicitly, or as a precaution against lightness in the meaning, as he, may his secret be sanctified, indicated."},

    # ---------------- Footnote 5 ----------------
    {"type": "note", "num": "٥"},
    {"type": "pair",
     "ar": "إشارة إلى فائدة لذكر قوله: «في اللفظ». وفيه بحثان:",
     "en": "This indicates a benefit in mentioning his words “in the wording.” There are two points for discussion in it:"},
    {"type": "pair",
     "ar": "أحدهما: أن المعنى لا يوصف بالخفة والثقل.",
     "en": "The first: meaning is not described by lightness and heaviness…"},
]
