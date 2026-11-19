# -*- coding: utf-8 -*-
"""Mulla Jami — al-Fawāʾid al-Ḍiyāʾiyya. Source PDF page 118 (printed ١١٧)."""

PAGE_NUMBER = 118
PRINTED_PAGE = "١١٧"   # Arabic-Indic, as printed

BLOCKS = [
    # ---------------- The main commentary (matn) ----------------
    {"type": "matn",
     "ar": "فإن مؤنثه «سكرى» لا «سكرانة».",
     "en": "for its feminine is “sakrā,” not “sakrāna.”"},
    {"type": "matn",
     "ar": "(و) دون (ندمان[[١]]) فإنه لا خلاف في صرفه، لانتفاء الشرط على المذهبين؛ لأن مؤنثه «ندمانة» لا «ندمى».",
     "en": "(And) unlike (nadmān, “boon-companion”) — for there is no disagreement over its full inflection, since the condition is absent on both positions, because its feminine is “nadmāna,” not “nadmā.”"},
    {"type": "matn",
     "ar": "هذا إذا كان «ندمان» بمعنى «النديم».",
     "en": "This is when “nadmān” has the sense of “nadīm” (boon-companion)."},
    {"type": "matn",
     "ar": "وأما إذا كان بمعنى النادم، فهو غير منصرف بالاتفاق؛ لأن مؤنثه «ندمى» لا «ندمانة».",
     "en": "But if it has the sense of “nādim” (one who regrets), then it is non-inflecting by consensus, because its feminine is “nadmā,” not “nadmāna.”"},

    # ---------------- Section heading ----------------
    {"type": "section", "ar": "[وزن الفعل]",
     "en": "The Pattern of the Verb"},

    {"type": "matn",
     "ar": "(وزن الفعل) وهو: «كون الاسم على وزن يعد من أوزان الفعل[[٢]]»، وهذا القدر لا يكفي في سببية منع الصرف، بل (شرطه) فيها أحد الأمرين:",
     "en": "(The pattern of the verb) — that is, “the noun’s being upon a pattern reckoned among the patterns of the verb.” Yet this much does not suffice for [establishing] its being a cause preventing full inflection; rather (its condition) in that regard is one of two things:"},
    {"type": "matn",
     "ar": "١- (إما أن يختص) في اللغة العربية (بالفعل) بمعنى[[٣]] أنه لا يوجد في الاسم العربي إلا منقولا من الفعل[[٤]] (كـ«شمر») على صيغة الفعل الماضي المعلوم من التشمير[[٥]]، فإنه نقل من هذه الصيغة، وجعل علما لفرس، وكذلك «عثر» لموضع[[٦]]،",
     "en": "1 — (Either that it be exclusive), in the Arabic language, (to the verb) — meaning that it does not occur in an Arabic noun except as transferred from a verb — (as in “shammara”), which is upon the form of the active-voice past-tense verb from tashmīr (girding oneself up); for it was transferred from this form and made a proper name of a horse; and likewise “ʿaththara” as [the name of] a place,"},

    {"type": "rule"},

    # ---------------- Footnotes ----------------
    {"type": "note", "num": "١"},
    {"type": "pair",
     "ar": "لما كان المراد بـ«ندمان» اللفظ كان علما غير منصرف، فينبغي ألا ينون ولا يكسر هنا إلا لمشاكلة المسمى.",
     "en": "Since what is intended by “nadmān” [here] is the wording [itself], it is a proper name that is non-inflecting, so it ought not to be given tanwīn nor a kasra here except to match [the pattern of] the thing named."},

    {"type": "note", "num": "٢"},
    {"type": "pair",
     "ar": "سواء كان له زيادة نسبة إلى الفعل أو لا. فالإضافة في قوله: «وزن الفعل» محمولة على النسبة لا على زيادة النسبة، وإلا لم يحتج إلى قوله: «فشرطه».",
     "en": "Whether or not it has an additional relation to the verb. So the genitive construction in his words “the pattern of the verb” is to be taken as [expressing merely] the relation, not the additional relation; otherwise there would have been no need for his words “so its condition.”"},
    {"type": "pair",
     "ar": "ولك أن تحمل عليها، وتحمل قوله: «فشرطه» على شرط التحقق لا على الاشتراط؛ لأن السببية ليست إلا للفرعية، ولا فرعية إلا فيما له زيادة اختصاص بالفعل.",
     "en": "You may, however, take it upon [the additional relation], and take his words “so its condition” as [referring to] the condition of realization, not [that of] stipulation; because being a cause pertains only to subordinacy, and there is no subordinacy except in that which has an additional exclusiveness to the verb."},

    {"type": "note", "num": "٣"},
    {"type": "pair",
     "ar": "في أكثر نسخ المتن به، والضمير راجع إلى الفعل، وضمير «يختص» راجع إلى الوزن أو بالعكس، وذا أعرب كما هو المشهور.",
     "en": "In most manuscripts of the base text it reads “bihi” (to it); and the [suffixed] pronoun refers to the verb, while the pronoun in “yakhtaṣṣu” refers to the pattern — or the reverse — and this is how it is parsed, as is well known."},

    {"type": "note", "num": "٤"},
    {"type": "pair",
     "ar": "وفهم ذلك من الاختصاص باعتبار أن المتبادر الاختصاص في اللغة العربية؛ لأن الكلام فيها، والمنقول من الفعل مستعار في الاسم، واستعارة الشيء من أحد لا يمنع اختصاص المستعار به،",
     "en": "That was understood from “exclusiveness” in view of the fact that what comes to mind first is exclusiveness within the Arabic language, because the discussion concerns it; and what is transferred from the verb is borrowed into the noun, and borrowing a thing from someone does not preclude the exclusiveness of that from which it is borrowed to it,"},
    {"type": "pair",
     "ar": "على أن لك أن تجعل كـ«شمر» قيدا للاختصاص، فتستفيد منه المراد بالاختصاص في هذا المقام.",
     "en": "besides which you may take “as in shammara” to be a qualification of the exclusiveness, thereby deriving from it what is intended by “exclusiveness” in this context."},

    {"type": "note", "num": "٥"},
    {"type": "pair",
     "ar": "وهو بمعنى المرور حادا أو مختالا أو التقليص على ما في القاموس.",
     "en": "It [tashmīr] means passing by swiftly, or strutting proudly, or drawing up [one’s garment], according to what is in al-Qāmūs."},
    {"type": "pair",
     "ar": "والمناسب بعلم الفرس أن يكون علما منقولا من معنى المرور حادا، والفرس فرس الحجاج، وكأنه لم يعينها تحاشيا عن ذكر الحجاج.",
     "en": "What befits [it being] the proper name of a horse is that it be a proper name transferred from the meaning of passing by swiftly; the horse is the horse of al-Ḥajjāj, and it is as though he did not specify it in order to avoid mentioning al-Ḥajjāj."},
    {"type": "pair",
     "ar": "والأظهر أن التمثيل بالعلم، وإلا فيحتمل أن يكون المقصود بالتمثيل شمر معروفا أو مجهولا كـ«ضرب»،",
     "en": "The more evident [view] is that the illustration is by [means of] the proper name; otherwise it is possible that what is intended by the illustration is “shammara” in the active or passive voice, like “ḍuriba,”"},
    {"type": "pair",
     "ar": "ويؤيد كونه علما تقدمه على «ضرب» مع كونه ثلاثيا مجردا؛ لأن التمثيل بـ«ضرب» مبني على فرض العلمية. وبـ«شمر» لتحقق اسميته، فهو أولى بالتقديم.",
     "en": "and its being a proper name is corroborated by its being placed before “ḍaraba,” despite the latter’s being a bare triliteral; because illustrating by “ḍaraba” is contingent upon the supposition of its being a proper name, whereas [illustrating] by “shammara” rests upon the [established] realization of its being a noun, so it is more fitting to be placed first."},

    {"type": "note", "num": "٦"},
    {"type": "pair",
     "ar": "في القاموس: هي مأسدة، وجعل معناه الفعلي جعله ذا كبوة.",
     "en": "In al-Qāmūs: it [ʿaththar] is a lions’ lair (maʾsada); and its verbal sense is taken to be his rendering it possessed of a stumble (kabwa)."},
]
