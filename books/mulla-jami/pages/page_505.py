# -*- coding: utf-8 -*-
"""Mulla Jami — al-Fawāʾid al-Ḍiyāʾiyya. Source PDF page 505 (printed ٥٠٤)."""

PAGE_NUMBER = 505
PRINTED_PAGE = "٥٠٤"   # Arabic-Indic, as printed

BLOCKS = [
    # ---------------- The commentary text (matn) ----------------
    # Continues «بل يجب أن يرفع» at the foot of PDF p. 504 (mid-sentence).
    {"type": "matn",
     "ar": "إما بالصفة إن كان صالحا للوصفية، كقوله تعالى: ﴿فهب لي من لدنك وليا يرثني﴾[[١]] فيمن قرأ مرفوعا أي: وليا وارثا،",
     "en": "…either as an attribute, if it is fit to qualify, as in His words, the Exalted, “So grant me from Yourself an heir who will inherit from me” (Qurʾān, Sūrat Maryam 19:5–6), in the reading of those who read it in the nominative, that is, “an heir inheriting”;"},
    {"type": "matn",
     "ar": "أو بالحال كذلك كقوله تعالى: ﴿ونذرهم في طغيانهم يعمهون﴾[[٢]]، أي: عمهين،",
     "en": "or as a circumstantial (ḥāl), likewise, as in His words, the Exalted, “And We leave them in their transgression, wandering blindly” (Qurʾān, Sūrat al-Anʿām 6:110), that is, “wandering blindly” [as a ḥāl];"},
    {"type": "matn",
     "ar": "أو بالاستئناف كقول الشاعر:",
     "en": "or as a fresh start (istiʾnāf), as in the poet’s saying:"},
    {"type": "verse",
     "ar": "وقال رائدهم أرسوا نزاولها          فكل حتف امرئ يجري بمقدار",
     "en": "Their scout said: “Cast anchor, let us grapple with it; for every man’s death runs by a fixed measure.”"},

    {"type": "section", "ar": "[فعل الأمر]",
     "en": "The Imperative Verb"},

    {"type": "matn",
     "ar": "(الأمر) هكذا في بعض النسخ.",
     "en": "(The command (al-amr)): so it is in some copies."},
    {"type": "matn",
     "ar": "وفي بعضها: «مثال الأمر»، وكان المراد به صيغة الأمر، فإنهم يطلقون أمثلة الماضي[[٣]] وأمثلة المضارع ويريدون صيغهما.",
     "en": "In some: “the form (mithāl) of the command”, and what is meant by it is the pattern of the command; for they say “the forms of the past” and “the forms of the muḍāriʿ” and mean their patterns."},
    {"type": "matn",
     "ar": "وفي بعض الشروح: إنما قال «مثال الأمر»؛ لأن الأمر كما اشتهر في هذا النوع من الأفعال اشتهر في المعنى المصدري[[٤]] أيضا، فأراد النص على المقصود[[٥]]،",
     "en": "In some commentaries: he said “the form of the command” only because “command”, just as it is well known for this kind of verb, is also well known in the sense of the verbal noun; so he wished to state explicitly what is intended;"},
    {"type": "matn",
     "ar": "وهو[[٦]] في اصطلاح النحويين والأصوليين مخصوص[[٧]] بالأمر بالصيغة، كذا ذكره المصنف في شرحه.",
     "en": "and in the terminology of the grammarians and the legal theorists (uṣūliyyūn) it is restricted to the command by the pattern. So the author mentioned in his commentary."},
    {"type": "matn",
     "ar": "(صيغة يطلب بها الفعل) شامل لكل أمر غائبا كان أو مخاطبا أو متكلما معلوما أو مجهولا",
     "en": "(A pattern by which an act is requested): this includes every command, whether third person, second person or first person, active or passive;"},
    {"type": "matn",
     "ar": "(من الفاعل) احتراز عن المجهول مطلقا، فإنه يطلب به الفعل عن المفعول لا عن الفاعل",
     "en": "(from the agent): this excludes the passive altogether, for by it the act is requested of the patient, not of the agent;"},
    {"type": "matn",
     "ar": "(المخاطب) احتراز عن الغائب والمتكلم (بحذف حرف المضارعة) احتراز",
     "en": "(the addressee): this excludes the third and first persons; (by omitting the prefix of the muḍāriʿ): this excludes…"},

    {"type": "rule"},

    # ---------------- Footnote 1 ----------------
    {"type": "note", "num": "١"},
    {"type": "pair",
     "ar": "سورة مريم: ٥-٦.",
     "en": "Qurʾān, Sūrat Maryam 19:5–6."},

    # ---------------- Footnote 2 ----------------
    {"type": "note", "num": "٢"},
    {"type": "pair",
     "ar": "سورة الأنعام: ١١٠.",
     "en": "Qurʾān, Sūrat al-Anʿām 6:110."},

    # ---------------- Footnote 3 ----------------
    {"type": "note", "num": "٣"},
    {"type": "pair",
     "ar": "أقوى الشاهد على إرادة الصيغة أنهم يقولون لهذا الأمر: الأمر بالصيغة.",
     "en": "The strongest evidence that the pattern is meant is that they call this command “the command by the pattern”."},
    {"type": "pair",
     "ar": "فقوله: مثال الأمر بمنزلة قولهم: الأمر بالصيغة.",
     "en": "So his phrase “the form of the command” is equivalent to their phrase “the command by the pattern”."},

    # ---------------- Footnote 4 ----------------
    {"type": "note", "num": "٤"},
    {"type": "pair",
     "ar": "الذي يشتق منه الماضي والمضارع وغيرهما.",
     "en": "From which the past, the muḍāriʿ and others are derived."},

    # ---------------- Footnote 5 ----------------
    {"type": "note", "num": "٥"},
    {"type": "pair",
     "ar": "من أول الأمر، فلا يرد أن الأمر المعرف بصيغة لا يحتمل المعنى المصدري، فزيادة لفظ المثال لدفع توهم إرادته توهم بعيد،",
     "en": "From the outset; so the objection does not hold that “command” defined by a pattern cannot bear the verbal-noun sense, so that adding the word “form” to ward off the supposition that it is meant is a far-fetched supposition;"},
    {"type": "pair",
     "ar": "وإنما أفاد النص؛ لأن إضافة الصيغة إلى ما بعده للبيان، كما في صيغة الماضي والمضارع وغيرهما،",
     "en": "it yields explicitness only because the annexation of the pattern to what follows it is explicative, as in “the pattern of the past”, “of the muḍāriʿ” and others;"},
    {"type": "pair",
     "ar": "فلا يرد أنه يجوز أن يكون الأمر بالمعنى المصدري حينئذ أيضا أي: صيغة الأمر كما يقال لام الأمر.",
     "en": "so the objection does not hold that “command” may then also be in the verbal-noun sense, that is, “the pattern of the command”, as one says “the lām of command”."},

    # ---------------- Footnote 6 ----------------
    {"type": "note", "num": "٦"},
    {"type": "pair",
     "ar": "أي: الأمر المطلق.",
     "en": "That is, “command” without qualification."},

    # ---------------- Footnote 7 ----------------
    {"type": "note", "num": "٧"},
    {"type": "pair",
     "ar": "لأن شرطه عند الأصوليين أن يكون مدلوله الطلب على وجه الاستعلاء دون النحويين، فإنهم يطلقونه على الصيغة بأي معنى يستعمل.",
     "en": "Because its condition among the legal theorists is that what it signifies be a request made from a position of superiority (istiʿlāʾ), unlike the grammarians, who apply it to the pattern in whatever sense it is used."},
]
