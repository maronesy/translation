# -*- coding: utf-8 -*-
"""Mulla Jami — al-Fawāʾid al-Ḍiyāʾiyya. Source PDF page 31 (printed ٣٠)."""

PAGE_NUMBER = 31          # PDF page
PRINTED_PAGE = "٣٠"       # page number printed in the book

BLOCKS = [
    # ---------------- The main commentary text (matn) ----------------
    {"type": "matn",
     "ar": "قيل: هي والكلام مشتقان من الكلم[[١]] -بتسكين اللام-: وهو الجرح[[٢]]، لتأثير معانيهما[[٣]] في النفوس كالجرح[[٤]].",
     "en": "It is said: it [al-kalima] and al-kalām are both derived from al-kalm — with a sukūn on the lām — which means “the wound,” on account of the effect their meanings have upon souls, just as a wound does."},
    {"type": "matn",
     "ar": "وقد عبر بعض الشعراء[[٥]] عن بعض تأثيراتهما[[٦]] بالجرح، حيث[[٧]] قال:",
     "en": "Some of the poets have expressed one of the two’s effects by [the word] al-jurḥ (wounding), when he said:"},

    {"type": "verse",
     "ar": "جراحات السنان[[٨]] لها التئام        ولا يلتام ما جرح اللسان[[٩]]",
     "en": "The wounds of spears may find healing, / but that which the tongue has wounded never heals."},

    {"type": "rule"},

    # ---- continuation of the previous page's (unnumbered) footnote ----
    {"type": "note", "num": "…"},
    {"type": "pair",
     "ar": "إنما يحصل بأن يقال في أول الأمر: الكلمة الكلمة كذا، فليس قوله: الكلمة كذا عقيب الابتداء أو التقديم، بل عقيب الإرادة.",
     "en": "It is realized only by saying, at the very outset: “al-kalima [is] the kalima such-and-such”; so his statement “al-kalima is such-and-such” does not [come] immediately after the commencing (ibtidāʾ) or the fronting (taqdīm), but rather immediately after the intention (irāda)."},
    {"type": "pair",
     "ar": "وقد جوز بعضهم أن يكون الفاء للتفسير، يعني: أن الابتداء بتعريف الكلمة أو التقديم لتعريفه هو القول في أول الأمر: الكلمة كذا.",
     "en": "Some have deemed it permissible for the fāʾ to be explicative (li-l-tafsīr), meaning: that the commencing with the definition of al-kalima — or the fronting for its definition — is [itself] the statement, at the very outset: “al-kalima [is] such-and-such.”"},

    # ---------------- Footnote 1 ----------------
    {"type": "note", "num": "١"},
    {"type": "pair",
     "ar": "أي: بالاشتقاق الصغير كما هو المتبادر عند الإطلاق، كاشتقاق صيغ الماضي، والمضارع، واسم الفاعل، والمفعول من المصدر.",
     "en": "That is, by the lesser derivation (al-ishtiqāq al-ṣaghīr), as is what comes readily to mind when [derivation] is used unrestrictedly — like the derivation of the forms of the past tense, the present tense, the active participle, and the passive participle from the verbal noun (maṣdar)."},
    {"type": "pair",
     "ar": "فاعلم أن الاشتقاق نزع لفظ من آخر بشروط أربعة:",
     "en": "Know, then, that derivation (ishtiqāq) is the extraction of one word from another under four conditions:"},
    {"type": "pair",
     "ar": "أحدها: أن يكون اللفظان متناسبين معنى بأن يكونا مشتركين في الدلالة على أصل المعنى.",
     "en": "The first: that the two words be congruent in meaning, in that they share in signifying the root meaning."},
    {"type": "pair",
     "ar": "ثانيها: أن يكونا متناسبين تركيبا بأن يشتملا على الحروف الأصلية.",
     "en": "The second: that they be congruent in structure, in that they comprise the [same] radical letters."},
    {"type": "pair",
     "ar": "وثالثها: أن يكونا متغايرين في الصيغة.",
     "en": "The third: that they differ in form."},
    {"type": "pair",
     "ar": "رابعها: أن يكون المشتق زائدا على المشتق منه بشيء من المعنى.",
     "en": "The fourth: that the derived word (mushtaqq) exceed that from which it is derived by some element of meaning."},
    {"type": "pair",
     "ar": "والمثال المشتمل على جميع ما ذكر «ضارب» مع ذكر «الضرب».",
     "en": "The example comprising all that has been mentioned is “ḍārib” (striker) together with the mention of “al-ḍarb” (striking)."},

    # ---------------- Footnote 2 ----------------
    {"type": "note", "num": "٢"},
    {"type": "pair",
     "ar": "الجرح -بفتح الجيم- مصدر «جرحه يجرحه» -بفتح العين- فيهما. وأما الجرح -بضم الجيم- فهو اسم بمعنى الجراحة.",
     "en": "Al-jarḥ — with a fatḥa on the jīm — is the verbal noun of “jaraḥahu yajraḥuhu” (he wounded him), with a fatḥa on the ʿayn in both. As for al-jurḥ — with a ḍamma on the jīm — it is a noun meaning “a wound” (al-jirāḥa)."},

    # ---------------- Footnote 3 ----------------
    {"type": "note", "num": "٣"},
    {"type": "pair",
     "ar": "أي: الكلمة والكلام.",
     "en": "That is: al-kalima and al-kalām."},

    # ---------------- Footnote 4 ----------------
    {"type": "note", "num": "٤"},
    {"type": "pair",
     "ar": "إن اكتفى بمطلق التأثير في التشبيه بالجرح يكون جاريا في الألفاظ باعتبار تأثيراتها الحسنة والسيئة،",
     "en": "If one is content with [the notion of] effect in an absolute sense in the likening to a wound, then it would apply to expressions with regard to their effects, both good and evil;"},
    {"type": "pair",
     "ar": "لكن قوله: «وقد عبر إلى آخره» يدل على أنه أراد التأثير بإحداث الألم، كما في تفسير البيضاوي في قوله تعالى:",
     "en": "but his words, “and [some of the poets] have expressed,” to the end [of the passage], indicate that he intended the effect [produced] by the causing of pain — as in al-Bayḍāwī’s exegesis of His words, the Exalted:"},
    {"type": "quran",
     "ar": "﴿فتلقى آدم من ربه كلمات فتاب عليه إنه هو التواب الرحيم﴾",
     "en": "“Then Adam received words from his Lord, and He turned toward him [in forgiveness]; indeed He is the Ever-Relenting, the Most Merciful” (Qurʾān, Sūrat al-Baqara 2:37)."},
    {"type": "pair",
     "ar": "أصل الكلمة الكلم، وهو التأثير المدرك بإحدى الحاستين: السمع، والبصر، كالكلام والجراحة.",
     "en": "The origin of al-kalima is al-kalm, which is the effect perceived by one of the two senses — hearing and sight — like speech and wounding."},

    # ---------------- Footnote 5 ----------------
    {"type": "note", "num": "٥"},
    {"type": "pair",
     "ar": "قال الشارح الكازروني: قائله أمير المؤمنين علي بن أبي طالب رضي الله عنه، ولم يبلغ ذلك الشارح، ولو بلغه لم يرض بأن يعبر عنه ببعض الشعراء.",
     "en": "The commentator al-Kāzarūnī said: its author is the Commander of the Faithful ʿAlī b. Abī Ṭālib, may Allah be pleased with him. This did not reach the [author of this] commentary; and had it reached him, he would not have been content to attribute it to “some of the poets.”"},

    # ---------------- Footnote 6 ----------------
    {"type": "note", "num": "٦"},
    {"type": "pair",
     "ar": "أي: الكلمة والكلام. هو التأثير بإحداث الألم المعبر عنه بالجرح.",
     "en": "That is: al-kalima and al-kalām; it is the effect [produced] by the causing of pain that is expressed by [the word] “wounding” (al-jarḥ)."},

    # ---------------- Footnote 7 ----------------
    {"type": "note", "num": "٧"},
    {"type": "pair",
     "ar": "يحتمل التعليل والمكان.",
     "en": "It [ḥaythu] admits [being for] causation (taʿlīl) or place (makān)."},

    # ---------------- Footnote 8 ----------------
    {"type": "note", "num": "٨"},
    {"type": "pair",
     "ar": "الجراحات جمع جراحة -بكسر الجيم-. والالتئام -مهموز العين-: البرء. والسنان -بالكسر-: الرمح.",
     "en": "Al-jirāḥāt is the plural of jirāḥa — with a kasra on the jīm. Al-iltiʾām — with a hamza on the [medial] radical — means “healing” (al-burʾ). Al-sinān — with a kasra — is “the spear” (al-rumḥ)."},

    # ---------------- Footnote 9 ----------------
    {"type": "note", "num": "٩"},
    {"type": "pair",
     "ar": "اللسان جاء بمعنى اللغة والجراحة المخصوصة، وكلاهما يحتمل ههنا.",
     "en": "Al-lisān is used with the meaning of “language” (al-lugha) and of a specific [kind of] wound; both are possible here."},
]
