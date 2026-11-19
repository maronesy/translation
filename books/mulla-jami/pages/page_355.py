# -*- coding: utf-8 -*-
"""Mulla Jami — al-Fawāʾid al-Ḍiyāʾiyya. Source PDF page 355 (printed ٣٥٤)."""

PAGE_NUMBER = 355
PRINTED_PAGE = "٣٥٤"   # Arabic-Indic, as printed

BLOCKS = [
    # ---------------- The commentary text (matn) ----------------
    # Continues «… بأنها إما بتضمن الاسم معنى مبني» at the foot of PDF p. 354.
    {"type": "matn",
     "ar": "الأصل[[١]] مثل: «أين»، فإنه يتضمن معنى همزة الاستفهام،",
     "en": "…by origin, as “ayna” (where?), for it includes the meaning of the interrogative hamza;"},
    {"type": "matn",
     "ar": "أو لشبهه له كالمبهمات، فإنها تشبه الحروف في الاحتياج إلى الصلة أو الصفة أو غيرهما[[٢]]،",
     "en": "or in its resembling it, as with the vague nouns (mubhamāt), for they resemble the particles in needing a relative clause, a qualifier or something else;"},
    {"type": "matn",
     "ar": "أو وقوعه موقعه كـ«نزال»، أو مشاكلته للواقع موقعه كـ«فجار»",
     "en": "or in its occupying its place, as “nazāli” (dismount!); or in its likeness to what occupies its place, as “fajāri” (wickedness);"},
    {"type": "matn",
     "ar": "أو وقوعه موقع ما يشبهه كالمنادى المضموم، فإنه واقع موقع كاف الخطاب المشابه للحرف في نحو: «أدعوك»،",
     "en": "or in its occupying the place of what resembles it, as the vocative with ḍamma, for it occupies the place of the kāf of address, which resembles the particle, in “adʿūka” (I call you);"},
    {"type": "matn",
     "ar": "أو إضافته إليه كقوله تعالى: ﴿من عذاب يومئذ﴾[[٣]] فيمن قرأ بالفتح",
     "en": "or in its being annexed to it, as in His words, Exalted is He, “from the punishment of that day” (min ʿadhābi yawmaʾidhin), according to those who read [yawma] with fatḥa."},
    {"type": "matn",
     "ar": "(أو وقع غير مركب) مع غيره على وجه يتحقق معه عامله،",
     "en": "(Or which occurs uncompounded) with anything else in such a way that its governor is realized with it."},
    {"type": "matn",
     "ar": "فعلى هذا المضاف من المركبات الإضافية المعدودة كـ«غلام زيد، وغلام عمرو، وغلام بكر» مبني، والمضاف إليه معرب.",
     "en": "On this basis the first term of genitive compounds that are merely listed, such as “ghulām Zayd, ghulām ʿAmr, ghulām Bakr”, is indeclinable, while the second term is declinable."},
    {"type": "matn",
     "ar": "ولما كان المبني مقابلا للمعرب، واعتبر فيه الأمران: «التركيب وعدم المشابهة لمبني الأصل» كان المبني ما انتفى فيه مجموع هذين الأمرين: إما بانتفائهما معا أو بانتفاء أحدهما فقط،",
     "en": "Since the indeclinable is the counterpart of the declinable, and in the latter two things were considered—“compounding and non-resemblance to what is indeclinable by origin”—the indeclinable is that in which the conjunction of these two is absent, either by the absence of both together or by the absence of one of them only."},
    {"type": "matn",
     "ar": "فكلمة «أو» ههنا لمنع الخلو[[٤]]،",
     "en": "So the word “aw” here is for excluding the absence of both (manʿ al-khuluww)."},
    {"type": "matn",
     "ar": "وإنما اختلف ترتيب ذكر المشابهة والتركيب في تعريفي المعرب والمبني تقديما وتأخيرا؛ إيثارا لتقدم ما مفهومه وجودي لشرفه.",
     "en": "The order in which resemblance and compounding are mentioned differs between the definitions of the declinable and the indeclinable, one placed first and the other later, out of preference for putting first what has an existential concept, because of its nobility."},
    {"type": "matn",
     "ar": "(وألقابه[[٥]]) أي: ألقاب المبني من حيث حركات أواخره[[٦]] وسكونها عند البصريين",
     "en": "(Its designations), that is, the designations of the indeclinable with respect to the vowels of its endings and their quiescence, according to the Baṣrans,"},
    {"type": "matn",
     "ar": "(ضم، وفتح، وكسر) للحركات الثلاث (ووقف[[٧]]) للسكون.",
     "en": "(are ḍamm, fatḥ and kasr) for the three vowels, (and waqf) for quiescence."},
    {"type": "matn",
     "ar": "وأما الكوفيون: فيذكرون ألقاب المبني في المعرب وبالعكس[[٨]]، والمراد أن",
     "en": "As for the Kūfans, they use the designations of the indeclinable for the declinable and vice versa. What is meant is that…"},

    {"type": "rule"},

    # ---------------- Footnote 1 ----------------
    {"type": "note", "num": "١"},
    {"type": "pair",
     "ar": "تحقيقا لا توهما، فلا يلزم بناء التثنية؛ لأن تضمنها لواو العطف وهمي لا حقيقي.",
     "en": "Really, not by supposition; so it does not follow that the dual is indeclinable, because its including the conjunctive wāw is supposed, not real."},

    # ---------------- Footnote 2 ----------------
    {"type": "note", "num": "٢"},
    {"type": "pair",
     "ar": "وهو الإشارة الحسية.",
     "en": "Namely, sensory pointing."},

    # ---------------- Footnote 3 ----------------
    {"type": "note", "num": "٣"},
    {"type": "pair",
     "ar": "سورة المعارج: ١١.",
     "en": "Qurʾān, Sūrat al-Maʿārij 70:11."},

    # ---------------- Footnote 4 ----------------
    {"type": "note", "num": "٤"},
    {"type": "pair",
     "ar": "لا للشك، فلا ينافي التعريف.",
     "en": "Not for doubt, so it is not incompatible with definition."},
    {"type": "pair",
     "ar": "إن قيل: في أي شق يدخل غاق في قولهم: غاق صوت الغراب؟",
     "en": "If it is asked: in which branch does “ghāq” fall in their saying “ghāq is the crow’s cry”?"},
    {"type": "pair",
     "ar": "أجيب عنه: بأنه غير مركب حكما باعتبار قصد المشاكلة للمبني الواقع غير مركب، وهو ما يتكلم به الصياد لا ما يرمي به الغراب من صوته؛",
     "en": "The answer given is that it is uncompounded by status, in view of the intended likeness to the indeclinable that occurs uncompounded, namely what the hunter utters, not the sound the crow casts out,"},
    {"type": "pair",
     "ar": "لأنه ليس بكلمة، فلا يكون معربا ولا مبنيا.",
     "en": "for that is not a word, and so is neither declinable nor indeclinable."},

    # ---------------- Footnote 5 ----------------
    {"type": "note", "num": "٥"},
    {"type": "pair",
     "ar": "عبر عن حركات البناء بالألقاب دون الأنواع لعدم اختلاف آثارها.",
     "en": "He expressed the vowels of indeclinability as “designations” rather than “kinds” because their effects do not differ."},

    # ---------------- Footnote 6 ----------------
    {"type": "note", "num": "٦"},
    {"type": "pair",
     "ar": "لا من حيث أنفسها، فإنه لا يقال: للمبني الضم ولا الفتح ولا الكسر،",
     "en": "Not with respect to [the vowels] themselves, for one does not say of the indeclinable “the ḍamm”, “the fatḥ” or “the kasr”,"},
    # REVIEW: «والمسكور» printed (evidently a misprint for «والمكسور»); transcribed as printed.
    {"type": "pair",
     "ar": "بل المضموم والمفتوح والمسكور ولا مطلقا؛",
     "en": "but rather “the one with ḍamm”, “the one with fatḥ” and “the one with kasr”; nor [are these designations used] without qualification,"},
    {"type": "pair",
     "ar": "لأن «يا زيدان» مبني على الألف، و«يا زيدون» على الواو ولا رجلين على الياء، ولا يقال لهذه الحروف: ضم وفتح وكسر.",
     "en": "because “yā Zaydāni” is indeclinable on the alif, “yā Zaydūna” on the wāw, and “lā rajulayni” on the yāʾ, and these letters are not called ḍamm, fatḥ and kasr."},

    # ---------------- Footnote 7 ----------------
    {"type": "note", "num": "٧"},
    {"type": "pair",
     "ar": "سمي الضم ضما لحصوله بضم الشفتين، والفتح فتحا لانفتاح الفم في التلفظ به،",
     "en": "Ḍamm was so called because it is produced by closing (ḍamm) the lips; fatḥ, because the mouth opens (infitāḥ) in pronouncing it;"},
    {"type": "pair",
     "ar": "والكسر كسرا لانكسار الشفة السفلى في التلفظ به. والوقف وقفا لتوقف النفس عن الجري.",
     "en": "kasr, because the lower lip breaks (inkisār) in pronouncing it; and waqf, because the breath stops (tawaqquf) from flowing."},

    # ---------------- Footnote 8 ----------------
    {"type": "note", "num": "٨"},
    {"type": "pair",
     "ar": "يعني: يطلقون الرفع والنصب والجر على الحركات البنائية.",
     "en": "He means: they apply rafʿ, naṣb and jarr to the vowels of indeclinability."},
]
