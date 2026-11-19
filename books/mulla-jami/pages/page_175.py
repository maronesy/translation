# -*- coding: utf-8 -*-
"""Mulla Jami — al-Fawāʾid al-Ḍiyāʾiyya. Source PDF page 175 (printed ١٧٤)."""

PAGE_NUMBER = 175
PRINTED_PAGE = "١٧٤"   # Arabic-Indic, as printed

BLOCKS = [
    # ---------------- The commentary text (matn) ----------------
    {"type": "matn",
     "ar": "إذا أردت الحال عن المفعول و«ضربي زيدا يلابسني قائما» إذا كان عن الفاعل أولى.",
     "en": "…if you intend the ḥāl [to refer] to the object, and “My beating Zayd accompanies me standing” if it [refers] to the agent, is preferable."},
    {"type": "matn",
     "ar": "ثم نقول: حذف المفعول الذي هو ذو الحال، فبقي: «ضربي زيدا يلابس قائما»،",
     "en": "Then we say: the object, which is the possessor of the ḥāl, was elided, and there remained: “My beating Zayd accompanies standing”;"},
    {"type": "matn",
     "ar": "ويجوز حذف ذي الحال مع قيام القرينة، تقول: «الذي ضربت قائما زيد» أي: «ضربته»،",
     "en": "for the elision of the possessor of the ḥāl is permissible when an indicator is present: you say “The one I struck standing is Zayd,” that is: “[whom] I struck him”;"},
    {"type": "matn",
     "ar": "ثم حذف «يلابس» الذي هو خبر المبتدأ والعامل في الحال، وقام الحال مقامه،",
     "en": "then “accompanies,” which is the predicate of the subject and the governor of the ḥāl, was elided, and the ḥāl took its place,"},
    {"type": "matn",
     "ar": "كما تقول: «راشدا مهديا» أي: «سر راشدا مهديا».",
     "en": "just as you say: “Rightly guided, well directed,” that is: “Go rightly guided, well directed.”"},
    {"type": "matn",
     "ar": "فعلى هذا يكونون مستريحين من تلك التكلفات البعيدة.",
     "en": "On this [account] they are relieved of those far-fetched strained constructions."},
    {"type": "matn",
     "ar": "وقال الكوفيون: تقديره: «ضربي زيدا قائما حاصل» بجعل «قائما» من متعلقات المبتدأ،",
     "en": "The Kūfans said: its implied form is “My beating Zayd standing takes place,” taking “standing” as one of the dependents of the subject;"},
    {"type": "matn",
     "ar": "ويلزمهم حذف الخبر من غير سد شيء مسده، وتقييد المبتدأ المقصود عمومه[[١]] بدليل الاستعمال.",
     "en": "this commits them to eliding the predicate with nothing filling its place, and to restricting a subject whose generality is intended, as usage shows."},
    {"type": "matn",
     "ar": "وذهب الأخفش[[٢]]: إلى أن الخبر الذي سدت الحال محله مصدر مضاف إلى صاحب الحال أي: «ضربي زيدا ضربه قائما»[[٣]].",
     "en": "Al-Akhfash held that the predicate whose place the ḥāl fills is a maṣdar annexed to the possessor of the ḥāl, that is: “My beating Zayd is his being beaten standing” (ḍarbī Zaydan ḍarbuhu qāʾiman)."},
    {"type": "matn",
     "ar": "وذهب بعضهم: إلى أن هذا المبتدأ لا خبر له[[٤]]، لكونه بمعنى الفعل[[٥]]؛ إذ المعنى: «ما أضرب زيدا إلا قائما»[[٦]].",
     "en": "Some held that this subject has no predicate, since it has the sense of a verb; for the meaning is: “I do not beat Zayd except standing.”"},
    {"type": "matn",
     "ar": "وثالثها: كل مبتدأ اشتمل[[٧]] خبره على معنى المقارنة، وعطف عليه شيء بالواو التي بمعنى «مع»",
     "en": "The third of them: every subject whose predicate comprises the sense of accompaniment (muqārana), and to which something has been conjoined by the wāw that means “with” (maʿa);"},
    {"type": "matn",
     "ar": "(و) ذلك مثل: («كل رجل وضيعته»[[٨]]) أي: «كل رجل مقرون مع",
     "en": "(and) that is as in: (“Every man and his craft”—kullu rajulin wa-ḍayʿatuhu), that is: “Every man is joined with…"},

    {"type": "rule"},

    # ---------------- Footnote 1 ----------------
    {"type": "note", "num": "١"},
    {"type": "pair",
     "ar": "اتفاقا. وذلك لأن اسم الجنس المعرف باللام إذا استعمل ولم تقم قرينة تخصصه ببعض ما يقع عليه،",
     "en": "By agreement. That is because when a generic noun (ism al-jins) made definite by the lām is used, and no indicator is present restricting it to some of what it applies to,"},
    {"type": "pair",
     "ar": "فهو الظاهر في الاستغراق دفعا للترجيح بلا مرجح.",
     "en": "it is evidently all-inclusive (istighrāq), to avoid preferring [one reading] without a ground for preference."},

    # ---------------- Footnote 2 ----------------
    {"type": "note", "num": "٢"},
    {"type": "pair",
     "ar": "يرد عليه أنه يلزم حذف المصدر مع بقاء معموله.",
     "en": "The objection to him is that it entails eliding the maṣdar while its governed element remains."},
    {"type": "pair",
     "ar": "وذلك ممتنع عندهم؛ لأنه في قوة أن الموصولة مع الفعل، ولا يجوز حذف الموصول مع بعض صلته.",
     "en": "That is impossible according to them, because it has the force of the relative (mawṣūla) “an” with the verb, and eliding the relative together with part of its relative clause (ṣila) is not permitted."},

    # ---------------- Footnote 3 ----------------
    {"type": "note", "num": "٣"},
    {"type": "pair",
     "ar": "ولا عيب فيه إلا أنهم لم يجوزوا حذف المصدر مع بقاء معموله؛",
     "en": "There is no fault in it, except that they did not permit eliding the maṣdar while its governed element remains;"},
    {"type": "pair",
     "ar": "لأنه كحذف \"أن\" مع الفعل مع بقاء معموله، وهو حذف الموصول مع بعض صلته، ولم يجوزوه.",
     "en": "because it is like eliding “an” with the verb while its governed element remains, which is eliding the relative with part of its relative clause, and they did not permit it."},

    # ---------------- Footnote 4 ----------------
    {"type": "note", "num": "٤"},
    {"type": "pair",
     "ar": "كما في القسم الثاني من المبتدأ.",
     "en": "As in the second category of the subject."},

    # ---------------- Footnote 5 ----------------
    {"type": "note", "num": "٥"},
    {"type": "pair",
     "ar": "يؤيده امتناع تأكيده بكل وأمثاله وامتناع توصيفه.",
     "en": "This is supported by the impossibility of corroborating it with “kull” and the like, and the impossibility of qualifying it."},

    # ---------------- Footnote 6 ----------------
    {"type": "note", "num": "٦"},
    {"type": "pair",
     "ar": "لا يخفى أن استفادة الحصر على هذا التقدير غير ظاهرة.",
     "en": "It is not hidden that obtaining restriction (ḥaṣr) on this supposition is not evident."},

    # ---------------- Footnote 7 ----------------
    {"type": "note", "num": "٧"},
    {"type": "pair",
     "ar": "قال الشيخ الرضي: الظاهر أن حذف الخبر في مثله غالب لا واجب.",
     "en": "Shaykh al-Raḍī said: what is apparent is that eliding the predicate in such [a case] is predominant, not obligatory."},
    {"type": "pair",
     "ar": "قال الكوفيون: إن الواو مع ما بعدها خبر؛ لأنها بمعنى \"مع\"، ولو أتى بـ\"مع\" كان خبرا، فكذا ما هو بمعناه.",
     "en": "The Kūfans said: the wāw together with what follows it is the predicate, because it means “with”; had one used “maʿa,” it would be the predicate, and so too what has its meaning."},
    {"type": "pair",
     "ar": "وفيه أن المعطوف لا يصح أن يكون خبرا.",
     "en": "Against this: the conjoined element (maʿṭūf) cannot validly be a predicate."},
    {"type": "pair",
     "ar": "ولا يجوز أن يقال: إعرابه منقول عن الواو؛ لأن مع إذا وقع خبرا لا يستحق الرفع لفظا حتى ينقل إلى ما بعده، بل يكون منصوبا.",
     "en": "Nor may it be said: its inflection is transferred from the wāw; because “maʿa,” when it occurs as a predicate, does not merit the nominative in its wording so as to transfer it to what follows; rather it is accusative."},

    # ---------------- Footnote 8 ----------------
    {"type": "note", "num": "٨"},
    {"type": "pair",
     "ar": "قال في الحاشية: الضيعة في اللغة العقار التي هي الأرض والنخل والمتاع.",
     "en": "He said in the Ḥāshiya: ḍayʿa in the language means real property (ʿaqār), namely land, palms and goods."},
    {"type": "pair",
     "ar": "وههنا كناية عن مصحفها، أعني الصنعة، انتهى.",  # REVIEW: printed «مصحفها» (checked at 700 dpi); sense taken as «مصحفها», the word of which ḍayʿa is a graphic variant (ṣanʿa)
     "en": "Here it is a metonymy (kināya) for its graphic variant (muṣḥafihā), I mean ṣanʿa (craft). End of quotation."},
    {"type": "pair",
     "ar": "إن قلت: لا يجوز رجوع الضمير في «ضيعته» إلى كل لظهور فساد المعنى، ولا",
     "en": "If you say: the pronoun in “ḍayʿatuhu” cannot refer back to “kull,” because the corruption of the meaning is evident, nor…"},
]
