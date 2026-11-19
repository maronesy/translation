# -*- coding: utf-8 -*-
"""Mulla Jami — al-Fawāʾid al-Ḍiyāʾiyya. Source PDF page 186 (printed ١٨٥)."""

PAGE_NUMBER = 186
PRINTED_PAGE = "١٨٥"   # Arabic-Indic, as printed

BLOCKS = [
    # ---------------- The commentary text (matn) ----------------
    {"type": "matn",
     "ar": "٣-(والعدد) إن دل على عدده[[١]].",
     "en": "3. (and [for] number—wa-l-ʿadad), if it indicates its number."},
    {"type": "matn",
     "ar": "(مثل: جلست جلوسا) للتأكيد، (وجلسة) بكسر الجيم للنوع (وجلسة) بفتحها للعدد.",
     "en": "(Such as: “I sat a sitting”—jalastu julūsan) for emphasis, (and “a [manner of] sitting”—wa-jilsatan) with kasra on the jīm, for kind, (and “a single sitting”—wa-jalsatan) with fatḥa on it, for number."},
    {"type": "matn",
     "ar": "(فالأول) أي: الذي للتأكيد (لا يثنى ولا يجمع)؛ لأنه دال[[٢]] على الماهية المعراة عن الدلالة على التعدد[[٣]]، والتثنية والجمع يستلزمان التعدد،",
     "en": "(So the first)—that is, the one for emphasis—(is neither dualized nor pluralized—lā yuthannā wa-lā yujmaʿu); because it indicates the quiddity (māhiyya) stripped of any indication of multiplicity, while dualization and pluralization entail multiplicity;"},
    {"type": "matn",
     "ar": "فلا يقال: «جلست جلوسين أو جلوسات» إلا إذا قصد به النوع أو العدد[[٤]]",
     "en": "so one does not say: “I sat two sittings or sittings” (jalastu julūsayni aw julūsātin), except when kind or number is intended by it,"},
    {"type": "matn",
     "ar": "(بخلاف أخويه) اللذين هما للنوع والعدد، نحو: «جلست جلستين أو جلسات» بكسر الجيم أو فتحها.",
     "en": "(unlike its two siblings—bi-khilāfi akhawayhi), which are for kind and number, as in: “I sat two sittings or [several] sittings” (jalastu jilsatayni aw jilsātin), with kasra or fatḥa on the jīm."},
    {"type": "matn",
     "ar": "(وقد يكون[[٥]]) المفعول المطلق (بغير لفظه[[٦]]) أي: مغايرا للفظ فعله[[٧]]:",
     "en": "(And it may be—wa-qad yakūnu), the absolute object, (in other than its wording—bi-ghayri lafẓihi), that is: differing from the wording of its verb:"},
    {"type": "matn",
     "ar": "١-إما بحسب المادة (نحو: قعدت جلوسا[[٨]]).",
     "en": "1. either in respect of the root material (mādda), (as in: “I sat down a sitting”—qaʿadtu julūsan);"},
    {"type": "matn",
     "ar": "٢-وإما بحسب الباب، مثل: «أنبته الله نباتا حسنا»[[٩]]،",
     "en": "2. or in respect of the verbal form (bāb), such as: “Allah caused it to grow a goodly growth” (anbatahu Allāhu nabātan ḥasanan);"},
    {"type": "matn",
     "ar": "وسيبويه يقدر له عاملا[[١٠]] من بابه، أي: «قعدت وجلست جلوسا» و«أنبته الله فنبت نباتا».",
     "en": "and Sībawayh supposes for it a governor of its own form, that is: “I sat down and sat a sitting” (qaʿadtu wa-jalastu julūsan) and “Allah caused it to grow, so it grew a growth” (anbatahu Allāhu fa-nabata nabātan)."},
    {"type": "matn",
     "ar": "(وقد يحذف الفعل) الناصب للمفعول المطلق (لقيام قرينة):",
     "en": "(And the verb may be elided)—the one that puts the absolute object in the accusative—(on account of the presence of a contextual indication—li-qiyāmi qarīnatin):…"},

    {"type": "rule"},

    # ---------------- Footnote 1 ----------------
    {"type": "note", "num": "١"},
    {"type": "pair",
     "ar": "أي: عدد الفعل لا عدد نوعه، وبهذا امتاز المثنى للنوع عن المثنى للفرد الشخصي.",
     "en": "That is: the number of the act, not the number of its kind; and by this the dual [denoting] kind is distinguished from the dual [denoting] the individual instance (al-fard al-shakhṣī)."},

    # ---------------- Footnote 2 ----------------
    {"type": "note", "num": "٢"},
    {"type": "pair",
     "ar": "هكذا قيل، والأظهر في العبارة أن يقال: لأنه دال على الماهية الغير القابلة للتعدد في نفسها،",
     "en": "Thus it has been said; but the clearer expression would be to say: because it indicates the quiddity, which in itself is not susceptible of multiplicity,"},
    {"type": "pair",
     "ar": "بخلاف فردها شخصيا كان أو نوعيا، فإنه قابل لذلك، ولهذا جاز تثنية أخويه وجمعهما لإرادة الفرد منهما.",
     "en": "unlike its individual instance, whether individual or specific, for that is susceptible of it; and for this reason the dualization and pluralization of its two siblings are permitted, since the individual instance is intended by them."},

    # ---------------- Footnote 3 ----------------
    {"type": "note", "num": "٣"},
    {"type": "pair",
     "ar": "وإلا لكان في مفهومه زيادة على مفهوم الفعل.",
     "en": "Otherwise there would be in its sense an addition to the sense of the verb."},

    # ---------------- Footnote 4 ----------------
    {"type": "note", "num": "٤"},
    # REVIEW: print reads «تحدد الأمثال» (no dot visible under the ḥāʾ); sense suggests تجدد "renewal"; transcribed as printed.
    {"type": "pair",
     "ar": "لا يكفي في قصد تعدد المصدر تحدد الأمثال من غير تخلل ما يقابله،",
     "en": "For intending a multiplicity of the maṣdar, the renewal of like instances is not sufficient without the intervention of what is opposed to it;"},
    {"type": "pair",
     "ar": "فلو قام زيد دائما ولم يجلس في تلك الأوقات كان ذلك قياما واحدا.",
     "en": "so if Zayd stood continuously and did not sit during those times, that would be a single standing."},

    # ---------------- Footnote 5 ----------------
    {"type": "note", "num": "٥"},
    {"type": "pair",
     "ar": "«قد» ههنا للتقليل؛ لأنه وإن كان كثيرا في نفسه قليل بالإضافة إلى ما إذا كان بلفظه،",
     "en": "“Qad” here is for diminution (taqlīl); because, although it is frequent in itself, it is infrequent relative to the case when it is in its [verb’s] wording;"},
    {"type": "pair",
     "ar": "أو للتكثير مجازا كما في قوله تعالى: ﴿قد نرى تقلب وجهك في السماء﴾ (سورة البقرة: ١٤٤).",
     "en": "or for multiplication (taksīr), figuratively, as in His saying, the Exalted: “We have seen the turning of your face toward the heaven” (Qurʾān, Sūrat al-Baqara 2:144)."},

    # ---------------- Footnote 6 ----------------
    {"type": "note", "num": "٦"},
    {"type": "pair",
     "ar": "وحينئذ كان أبلغ وأوكد مما كان بلفظه.",
     "en": "In that case it is more eloquent and more emphatic than what is in its [verb’s] wording."},

    # ---------------- Footnote 7 ----------------
    {"type": "note", "num": "٧"},
    {"type": "pair",
     "ar": "وهو إما مصدر أو غير مصدر. وقد مر أمثلته.",
     "en": "It is either a maṣdar or other than a maṣdar; its examples have already passed."},
    {"type": "pair",
     "ar": "ومنها الضمير الراجع إلى مضمون عامله أو غير عامله، نحو: «يدرسه» أي: الدرس، وأعجبني الضرب الذي ضربته.",
     "en": "Among them is the pronoun referring to the content of its governor or of other than its governor, as in: “yadrusuhu” (he studies it), that is, the study; and “The striking that I struck pleased me.”"},
    {"type": "pair",
     "ar": "ومنها اسم إشارة المشار به إلى غير مضمون عامله، نحو: «أعجبني ضربي فضربت ذاك».",
     "en": "Among them is the demonstrative noun by which reference is made to other than the content of its governor, as in: “My striking pleased me, so I struck that [striking]” (fa-ḍarabtu dhāka)."},

    # ---------------- Footnote 8 ----------------
    {"type": "note", "num": "٨"},
    {"type": "pair",
     "ar": "قد يفرق بين القعود والجلوس بأن القعود للقائم والجلوس للنائم.",
     "en": "A distinction is sometimes drawn between qaʿūd and julūs, in that qaʿūd [sitting down] is said of one standing and julūs [sitting up] of one lying down."},

    # ---------------- Footnote 9 ----------------
    {"type": "note", "num": "٩"},
    {"type": "pair",
     "ar": "فإنه مصدر «نبت»، فجعل منصوبا بـ«أنبت»",
     "en": "For it is the maṣdar of “nabata” (it grew), and it has been made accusative by “anbata” (he caused to grow),"},
    {"type": "pair",
     "ar": "إما لأنه في ضمنه لأن معنى «أنبت» جعله ذا نبات ينبت، وأنه مطاوع له،",
     "en": "either because it is contained in it, since the meaning of “anbata” is: He made it possessed of growth, [so that] it grows; and [because nabata] is its reflexive counterpart (muṭāwiʿ);"},
    {"type": "pair",
     "ar": "أو لأنه جعل بمعنى الإنبات، وفيه تأمل.",
     "en": "or because it has been made to bear the sense of inbāt (causing to grow); and there is matter for reflection in this."},
    {"type": "pair",
     "ar": "وقيل: إنه بمعنى التنبيت كالسلام بمعنى التسليم.",
     "en": "It has been said: it has the sense of tanbīt, like salām in the sense of taslīm."},
    {"type": "pair",
     "ar": "وقيل: إنه ليس من هذا الباب؛ لأنه مغير إنبات.",
     "en": "And it has been said: it is not of this category, because it is an altered form of inbāt."},

    # ---------------- Footnote 10 ----------------
    {"type": "note", "num": "١٠"},
    {"type": "pair",
     "ar": "أي: في ما عدا مثل: «ضربته أنواعا»، الظاهر مع سيبويه في مثل: «أنبت الله نباتا» دون مثل: «قعدت جلوسا».",
     "en": "That is: in what is other than such as “I struck him [with] kinds [of striking].” The apparent [view] sides with Sībawayh in such as “Allah caused growth” (anbata Allāhu nabātan), not in such as “I sat down a sitting” (qaʿadtu julūsan)."},
]
