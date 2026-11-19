# -*- coding: utf-8 -*-
"""Mulla Jami — al-Fawāʾid al-Ḍiyāʾiyya. Source PDF page 189 (printed ١٨٨)."""

PAGE_NUMBER = 189
PRINTED_PAGE = "١٨٨"   # Arabic-Indic, as printed

BLOCKS = [
    # ---------------- The commentary text (matn) ----------------
    {"type": "matn",
     "ar": "داخل[[١]] على اسم[[٢]] لا يكون) المفعول المطلق (خبرا عنه[[٣]]) أي: عن ذلك الاسم.",
     "en": "…entering upon a noun of which) the absolute object (cannot be the predicate—lā yakūnu khabaran ʿanhu), that is: of that noun."},
    {"type": "matn",
     "ar": "وإنما قال: «على الاسم»؛ لأنه لو دخل على فعل نحو: «ما سرت إلا سيرا» و«إنما سرت سيرا» لا يكون منه.",
     "en": "He said “upon a noun” only because, if it entered upon a verb, as in: “I did not go except a going” (mā sirtu illā sayran) and “I only went a going” (innamā sirtu sayran), it would not be of this [class]."},
    {"type": "matn",
     "ar": "وإنما وصف الاسم بألا يكون المفعول المطلق خبرا عنه؛ لأنه لو كان خبرا عنه نحو: «ما سيري إلا سير شديد» لكان مرفوعا على الخبرية[[٤]]",
     "en": "He qualified the noun as one of which the absolute object cannot be the predicate only because, if it were its predicate, as in: “My going is nothing but a hard going” (mā sayrī illā sayrun shadīdun), it would be in the nominative as a predicate."},
    {"type": "matn",
     "ar": "(أو وقع) المفعول المطلق (مكررا[[٥]]) أي: في موضع الخبر[[٦]] عن اسم لا يصلح وقوعه خبرا عنه[[٧]]،",
     "en": "(Or) the absolute object (occurs repeated—mukarraran), that is: in the position of the predicate of a noun of which it is not fit to occur as the predicate;"},
    {"type": "matn",
     "ar": "فلا يرد عليه نحو: ﴿كلا إذا دكت الأرض دكا دكا﴾[[٨]]،",
     "en": "so an example such as “No! When the earth is pounded, pounding upon pounding” is no objection to it."},
    {"type": "matn",
     "ar": "وإنما جمع بين الضابطتين[[٩]] لاشتراكهما في الوقوع بعد اسم لا يكون خبرا عنه[[١٠]]",
     "en": "He combined the two criteria only because they share in occurring after a noun of which it cannot be the predicate:"},
    {"type": "matn",
     "ar": "(نحو: ما أنت إلا سيرا) أي: «تسير سيرا» (وما أنت إلا سير البريد) أي: «تسير سير البريد».",
     "en": "(as in: “You are nothing but going”—mā anta illā sayran), that is: “you go a going”; (and “You are nothing but the going of the courier”—wa-mā anta illā sayra al-barīd), that is: “you go the going of the courier.”"},
    {"type": "matn",
     "ar": "هذان مثالان",
     "en": "These are two examples…"},

    {"type": "rule"},

    # ---------------- Footnote 1 ----------------
    {"type": "note", "num": "١"},
    {"type": "pair",
     "ar": "قيل: صفة لـ«نفي». والأظهر: أن يقال: صفة لكل من نفي ومعنى نفي.",
     "en": "It has been said: [dākhilin] is an adjective of “nafy” (negation). The more evident is to say: it is an adjective of each of “negation” and “the sense of negation.”"},

    # ---------------- Footnote 2 ----------------
    {"type": "note", "num": "٢"},
    {"type": "pair",
     "ar": "مبتدأ أو منسوخ ابتداؤه بالعامل.",
     "en": "[A noun that is] a mubtadaʾ, or one whose status as mubtadaʾ has been abrogated by a governor."},
    {"type": "pair",
     "ar": "قال الشيخ الرضي: دخول النفي على الاسم المذكور ليس بشرط،",
     "en": "Shaykh al-Raḍī said: the entry of the negation upon the aforementioned noun is not a condition,"},
    {"type": "pair",
     "ar": "لجواز أن يكون في نحو: «ما كان زيد إلا سيرا» و«ما وجدتك إلا سير البريد» انتصاب المصدر على أنه مفعول مطلق كما جاز أن يكون منصوبا بـ«كان» أو «وجد»،",
     "en": "since it is possible that in such as “Zayd was nothing but going” and “I found you nothing but the going of the courier,” the maṣdar is accusative as an absolute object, just as it is possible that it be made accusative by “kāna” or “wajada”;"},
    {"type": "pair",
     "ar": "فالشرط أن يكون ناصبه خبرا عن شيء لا يكون هو، أي: المصدر خبرا عنه.",
     "en": "so the condition is that what puts it in the accusative be the predicate of something of which it—that is, the maṣdar—is not the predicate."},

    # ---------------- Footnote 3 ----------------
    {"type": "note", "num": "٣"},
    {"type": "pair",
     "ar": "أي: داخل على طالب للخبر، ولا يكون المصدر خبرا عنه لعدم قصد المتكلم خبريته.",
     "en": "That is: entering upon what requires a predicate, while the maṣdar is not its predicate, because the speaker does not intend it as predicate."},
    {"type": "pair",
     "ar": "والمراد بالدخول الدخول صورة أو معنى ليشمل «ما كان زيد إلا سيرا» بمعنى «إلا يسير سيرا»،",
     "en": "What is meant by “entering” is entering in form or in sense, so that it includes “Zayd was nothing but going” in the sense of “except that he goes a going”;"},
    {"type": "pair",
     "ar": "فإن النفي وإن لم يدخل على زيد لفظا، لكنه داخل معنى؛ لأنه لنفي السير عن زيد كما في «ما زيد إلا سيرا»",
     "en": "for the negation, although it does not enter upon Zayd verbally, does enter [upon it] in sense, since it is for negating going of Zayd, as in “Zayd is nothing but going.”"},
    {"type": "pair",
     "ar": "وخرج بقولنا: لا يكون خبرا عنه بقصد المتكلم، نحو: «ما زيد إلا سير» بالرفع.",
     "en": "By our saying “it is not its predicate by the speaker’s intention” is excluded such as “Zayd is nothing but going” (mā Zaydun illā sayrun) in the nominative."},
    {"type": "pair",
     "ar": "وقيل: المعنى لا يصلح أن يكون خبرا بلا تأويل أو مبالغة،",
     "en": "It has been said: the meaning is that it is not fit to be a predicate without interpretation (taʾwīl) or intensification;"},
    {"type": "pair",
     "ar": "وفيه نظر؛ لأنه يصدق مع ذلك «ما زيد إلا سير» مع أنه ليس محذوف الفعل.",
     "en": "but this is open to objection, because “Zayd is nothing but going” (with the nominative) also satisfies that, although its verb is not elided."},

    # ---------------- Footnote 4 ----------------
    {"type": "note", "num": "٤"},
    {"type": "pair",
     "ar": "قيل: فلا يكون مفعولا مطلقا؛ لأنه مرفوع. ورد بأن المفعول المطلق قد يرفع بالقيام مقام الفاعل؟",
     "en": "It has been said: so it would not be an absolute object, because it is nominative. This was rejected on the ground that the absolute object is sometimes put in the nominative by standing in place of the agent?"},
    {"type": "pair",
     "ar": "قلت: لا يكون مفعولا مطلقا؛ لأنه معمول للعامل المعنوي، والمفعول المطلق لا يكون كذلك،",
     "en": "I say: it is not an absolute object, because it is governed by the abstract governor (al-ʿāmil al-maʿnawī), and the absolute object is not so [governed];"},
    {"type": "pair",
     "ar": "وفيه نظر، فالأولى أن يمثل بما حالك إلا سيرا شديدا، فإن حذف فعله لا يجب، بل يصح ما حالك إلا أن تسير سيرا شديدا.",
     "en": "but this is open to objection. It would be better to exemplify with “Your state is nothing but hard going” (mā ḥāluka illā sayran shadīdan), for the elision of its verb is not obligatory; rather, “Your state is nothing but that you go a hard going” is correct."},

    # ---------------- Footnote 5 ----------------
    {"type": "note", "num": "٥"},
    {"type": "pair",
     "ar": "لو قال: أو مكررا بالعطف على «مثبتا» لكان أخصر إلا أنه احترز عن توهم عطفه على قوله: «خبرا».",
     "en": "Had he said “or repeated,” coordinating it with “muthbatan,” it would have been more concise; but he guarded against the misconception that it is coordinated with his word “khabaran.”"},

    # ---------------- Footnote 6 ----------------
    {"type": "note", "num": "٦"},
    {"type": "pair",
     "ar": "لا يخفى أن العبارة لا تفيد هذا القيد إلا بتكلف.",
     "en": "It is not hidden that the wording does not convey this qualification except with strain (takalluf)."},

    # ---------------- Footnote 7 ----------------
    {"type": "note", "num": "٧"},
    # REVIEW: print clearly reads «لا نفي العبارة»; probably a misprint for «لا تفي العبارة» ("the wording does not fulfil"); translated on that reading.
    {"type": "pair",
     "ar": "لا يخفى أنه لا نفي العبارة بتقدير هذا،",
     "en": "It is not hidden that the wording does not fulfil the supposition of this;"},
    {"type": "pair",
     "ar": "وكأنه جعل المصنف ضمير «وقع» راجعا إلى مفعول مطلق وقع بعد اسم لا يكون خبرا عنه؛ لأنه مما ذكر ضمنا، لكنه بعيد أيضا.",
     "en": "it is as though the author made the pronoun of “waqaʿa” refer to an absolute object occurring after a noun of which it is not the predicate, since that is among what was mentioned implicitly; but this too is far-fetched."},
    {"type": "pair",
     "ar": "والأخصر الأوضح هو أن يقال: مما وقع مثبتا بـ«إلا» أو معناه أو مكررا لا يكون خبرا عنه.",
     "en": "The most concise and clearest would be to say: “of what occurs affirmed by illā or its sense, or repeated, not being the predicate of it.”"},

    # ---------------- Footnote 8 ----------------
    {"type": "note", "num": "٨"},
    {"type": "pair",
     "ar": "سورة الفجر: ٢١.",
     "en": "Qurʾān, Sūrat al-Fajr 89:21."},

    # ---------------- Footnote 9 ----------------
    {"type": "note", "num": "٩"},
    {"type": "pair",
     "ar": "لا يخفى أنهما قد يجتمعان نحو: «ما زيد إلا سيرا سيرا»، وحينئذ ينبغي أن يقال: إن الحذف أوجب.",
     "en": "It is not hidden that the two may combine, as in: “Zayd is nothing but going, going” (mā Zaydun illā sayran sayran); in that case one should say that the elision is all the more obligatory."},

    # ---------------- Footnote 10 ----------------
    {"type": "note", "num": "١٠"},
    {"type": "pair",
     "ar": "فيه أنه يقتضي أن يجمع بين قاعدتي ما وقع مضمون جملة لاشتراكهما في الوقوع مضمون جملة.",
     "en": "Against this: it would require combining the two rules of what occurs as the content of a sentence, because they share in occurring as the content of a sentence."},
]
