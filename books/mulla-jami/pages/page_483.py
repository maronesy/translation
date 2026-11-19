# -*- coding: utf-8 -*-
"""Mulla Jami — al-Fawāʾid al-Ḍiyāʾiyya. Source PDF page 483 (printed ٤٨٢)."""

PAGE_NUMBER = 483
PRINTED_PAGE = "٤٨٢"   # Arabic-Indic, as printed

BLOCKS = [
    # ---------------- The commentary text (matn) ----------------
    # Continues the list of the verb's properties from PDF p. 482 (new item).
    {"type": "matn",
     "ar": "٤-(ولحوق تاء التأنيث) عطف على «دخول قد».",
     "en": "4. (And the attachment of the tāʾ of the feminine) is coordinated with “the entry of qad”."},
    {"type": "matn",
     "ar": "وإنما خص به لحوق تاء التأنيث؛ لأنها تدل على تأنيث الفاعل، ولا تلحق إلا بما له فاعل،",
     "en": "The attachment of the tāʾ of the feminine is specific to it only because it indicates that the agent is feminine, and it attaches only to what has an agent;"},
    {"type": "matn",
     "ar": "والصفات استغنت عنها بما لحقها من تاء المتحركة الدالة على تأنيثها، وتأنيث فاعلها، فلا جرم اختصت بالفعل،",
     "en": "and adjectives dispense with it through the voweled tāʾ attached to them, which indicates their own femininity and that of their agent; so it is necessarily specific to the verb."},
    {"type": "matn",
     "ar": "(ساكنة) حال عن «تاء التأنيث»[[١]]، احتراز عن المتحركة لاختصاصها بالاسم.",
     "en": "(Quiescent) is a circumstantial qualifier of “the tāʾ of the feminine”, a precaution against the voweled one, since that is specific to the noun."},
    {"type": "matn",
     "ar": "٥-(و) لحوق (نحو: تاء «فعلت») أراد بـ«نحو: تاء فعلت» الضمائر المتصلة البارزة المتحركة المرفوعة.",
     "en": "5. (And) the attachment of (the like of the tāʾ of “faʿaltu”): by “the like of the tāʾ of faʿaltu” he meant the attached, visible, voweled pronouns in the nominative."},
    {"type": "matn",
     "ar": "فيدخل فيه أيضا نون «فعلن» أيضا،",
     "en": "So the nūn of “faʿalna” is also included in it."},
    {"type": "matn",
     "ar": "وذلك لأن ضمير الفاعل لا يلحق إلا بما له فاعل، والفاعل إنما يكون للفعل وفروعه،",
     "en": "That is because the agent pronoun attaches only to what has an agent, and an agent belongs only to the verb and its derivatives;"},
    {"type": "matn",
     "ar": "وحط فروعه عنه بمنع أحد نوعي الضمير تحرزا عن لزوم تساوي الفرع والأصل.",
     "en": "and its derivatives were placed below it by being denied one of the two kinds of pronoun, to avoid the consequence that derivative and origin be equal."},
    {"type": "matn",
     "ar": "وخص البارز بالمنع؛ لأن المستكن أخف وأخصر، فهو بالتعميم أليق وأجدر.",
     "en": "The visible [pronoun] was singled out for denial because the concealed one is lighter and shorter, and so more fitting and worthy of being general."},

    {"type": "section", "ar": "[الفعل الماضي]",
     "en": "The Past Verb (al-Māḍī)"},

    {"type": "matn",
     "ar": "(الماضي: ما دل) أي: فعل دل بحسب أصل الوضع، فإنه المتبادر من الدلالة",
     "en": "(The past is what indicates), that is, a verb that indicates by its original coining, for this is what first comes to mind from “indication”,"},
    {"type": "matn",
     "ar": "(على زمان قبل زمانك) الحاضر الذي أنت فيه قبلية ذاتية يكون بين أجزاء الزمان،",
     "en": "(a time before your time), the present in which you are, with an essential priority (qabliyya dhātiyya) such as obtains between the parts of time;"},
    {"type": "matn",
     "ar": "فإن تقدم بعض أجزاء الزمان على بعض، إنما يكون بحسب الذات لا بحسب الزمان، فلا يلزم أن يكون للزمان زمان.",
     "en": "for the priority of some parts of time over others is only by essence, not by time; so it does not follow that time has a time."},
    {"type": "matn",
     "ar": "فقوله: «ما دل على زمان» شامل لجميع الأفعال.",
     "en": "His words “what indicates a time” cover all verbs."},
    {"type": "matn",
     "ar": "وقوله: «قبل زمانك» يخرج ما عداه.",
     "en": "His words “before your time” exclude everything else."},
    {"type": "matn",
     "ar": "والمراد بالموصول «الفعل»، فلا ينتقض منع الحد بمثل: «أمس»،",
     "en": "What is meant by the relative is “the verb”; so the definition’s exclusiveness is not broken by the like of “ams” (yesterday);"},
    {"type": "matn",
     "ar": "وبالدلالة ما هو بحسب الوضع، فلا ينتقض منعه بـ«لم يضرب»، وجمعه بـ«إن ضربت ضربت».",
     "en": "and by “indication” what is by coining is meant, so its exclusiveness is not broken by “lam yaḍrib” (he did not strike), nor its comprehensiveness by “in ḍarabta ḍarabtu” (if you strike, I will strike)."},
    {"type": "matn",
     "ar": "(مبني على الفتح[[٢]]) خبر لمبتدأ محذوف[[٣]]، أي: هو يعني: الماضي مبني على",
     "en": "(Indeclinable on the fatḥa) is the predicate of an elided inchoative, that is, “it”, meaning: the past is indeclinable on…"},

    {"type": "rule"},

    # ---------------- Footnote 1 ----------------
    {"type": "note", "num": "١"},
    {"type": "pair",
     "ar": "وفيه إشارة إلى أنها في الأصل متحركة أسكنت للفرق بين تأنيث الاسم والفعل، كما في الرضي،",
     "en": "In it is an indication that it is originally voweled and was made quiescent to distinguish between the feminine of the noun and of the verb, as in al-Raḍī;"},
    {"type": "pair",
     "ar": "وفي بعض النسخ: الساكنة باللام.",
     "en": "and in some copies: “al-sākina”, with the article."},

    # ---------------- Footnote 2 ----------------
    {"type": "note", "num": "٢"},
    {"type": "pair",
     "ar": "أشار إلى بيان بعض خواصه بعد تعريفه كما هو عادته.",
     "en": "He turned to setting out some of its properties after its definition, as is his custom."},

    # ---------------- Footnote 3 ----------------
    {"type": "note", "num": "٣"},
    {"type": "pair",
     "ar": "ولم يجعله خبرا بعد خبر رعاية لجانب المعنى؛",
     "en": "He did not make it a predicate after a predicate, out of regard for the meaning;"},
    {"type": "pair",
     "ar": "لأن الحد ليس خبرا عن المحدود من حيث المعنى لعدم كون الحكم مقصودا كما تقرر في موضعه،",
     "en": "for the definition is not a predicate of the thing defined in respect of meaning, since no judgement is intended, as has been established in its place;"},
    {"type": "pair",
     "ar": "ومن جوز كونه خبرا بعد خبر نظرا إلى جانب اللفظ، فقد سها.",
     "en": "and whoever allowed it to be a predicate after a predicate, looking to the wording, has erred."},
]
