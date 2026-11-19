# -*- coding: utf-8 -*-
"""Mulla Jami — al-Fawāʾid al-Ḍiyāʾiyya. Source PDF page 111 (printed ١١٠)."""

PAGE_NUMBER = 111
PRINTED_PAGE = "١١٠"   # Arabic-Indic, as printed

BLOCKS = [
    # ---------------- The base text (matn) ----------------
    {"type": "matn",
     "ar": "فأجاب: بأنه قد اختلف في صرفه ومنعه منه، فهو (إذا لم يصرف، وهو الأكثر[[١]]) في موارد الاستعمال[[٢]]، فيرد به الإشكال على قاعدة الجمع، كما قلت.",
     "en": "He answered: [scholars] have differed over declining it (ṣarf) and withholding declension from it; so, [in the words of the Kāfiya,] “when it is not declined — and this is the more frequent [usage]” in the instances of usage, the difficulty is thereby raised against the rule of the [broken] plural, just as I said."},

    {"type": "matn",
     "ar": "(فقد قيل) في التفصي عنه: (إنه) اسم (أعجمي[[٣]]) ليس بجمع، لا في الحال، ولا في الأصل، (حمل) في منع الصرف (على موازنه[[٤]]) أي: على ما يوازنه من الجموع العربية، كـ«أناعيم ومصابيح»،",
     "en": "“It has [therefore] been said,” in seeking to extricate oneself from it: “that it is a foreign (aʿjamī) noun,” not a plural — neither in its present state nor in its origin — [and that] “it was assimilated,” in respect of the withholding of declension, “to what parallels it [in pattern]”; that is, to the Arabic plurals that share its measure, such as anāʿīm and maṣābīḥ."},

    {"type": "matn",
     "ar": "فإنه في حكمهما من حيث الوزن، فهو وإن لم يكن من قبيل الجمع حقيقة، لكنه من قبيله حكما[[٥]]، فالجمعية على هذا التقدير أعم من أن تكون حقيقية أو حكمية،",
     "en": "For it takes their ruling with respect to pattern; so, even though it does not belong to the category of the plural in reality, it belongs to it by legal effect (ḥukman). On this reckoning, then, plurality is more general than being either real or [merely] by legal effect;"},

    {"type": "matn",
     "ar": "فبناء هذا الجواب على تعميم الجمعية لا على زيادة سبب آخر على الأسباب التسعة، وهو الحمل على الموازن.",
     "en": "so this answer rests upon broadening [the concept of] plurality, not upon adding another cause to the nine causes [that prevent declension] — namely, assimilation to the parallel [pattern]."},

    {"type": "matn",
     "ar": "(وقيل) هو اسم (عربي) ليس بجمع تحقيقا؛ لأنه اسم جنس يطلق على الواحد والكثير، لكنه (جمع سروالة تقديرا[[٦]]) وفرضا،",
     "en": "“And it has [also] been said” that it is an Arabic noun, not a plural in fact — for it is a generic noun (ism jins) applied to both the single and the many — but that it is “the plural of sirwāla by supposition (taqdīran)” and hypothetically;"},

    {"type": "matn",
     "ar": "فإنه لما وجد غير منصرف، ومن قاعدتهم: أن هذا الوزن بدون الجمعية لم يمنع الصرف قدر حفظا لهذه القاعدة أنه جمع «سروالة»، فكأنه سمي كل قطعة من السراويل سروالة[[٧]]، ثم جمعت سروالة على سراويل.",
     "en": "for since it was found to be non-declinable, while it is one of their rules that this pattern, without plurality, does not prevent declension, it was posited — to preserve this rule — that it is the plural of “sirwāla,” as though each piece of the trousers (sarāwīl) were named “sirwāla,” and then “sirwāla” was pluralized as “sarāwīl.”"},

    {"type": "rule"},

    # ---------------- Footnote 1 ----------------
    {"type": "note", "num": "١"},
    {"type": "pair",
     "ar": "الضمير لعدم الصرف، أي: عدم صرفه الأكثر. ولا حاجة إلى تقدير قوله: في موارد الاستعمال، وجعله في تقدير، وهو مذهب الأكثر بعيد جدا لا يفهم،",
     "en": "The pronoun refers to the non-declension; that is, its non-declension is the more frequent [case]. There is no need to supply his phrase “in the instances of usage” and to treat it as understood — for [taking it to mean] that it is the doctrine of the majority is very far-fetched and unintelligible;"},
    {"type": "pair",
     "ar": "وصحته يتوقف على ثبوت اختلاف النحاة فيه، وهو وإن اشتهر ففيه شيء.",
     "en": "and its soundness depends on establishing that the grammarians differed over it, and even if that is well known, there is [still] something [questionable] in it."},

    # ---------------- Footnote 2 ----------------
    {"type": "note", "num": "٢"},
    {"type": "pair",
     "ar": "أو مذهب الأكثر.",
     "en": "Or [it is] the doctrine of the majority."},

    # ---------------- Footnote 3 ----------------
    {"type": "note", "num": "٣"},
    {"type": "pair",
     "ar": "خبر مبتدأ محذوف.",
     "en": "[It is] the predicate of an omitted subject (mubtadaʾ)."},

    # ---------------- Footnote 4 ----------------
    {"type": "note", "num": "٤"},
    {"type": "pair",
     "ar": "لأنه دخيل، والدخيل يميل إلى المجانس، وإنما لم يمنع من الصرف آجر المعرب مخففا حملا على موازنة من أفعل علما؛ لأن جميع ما يوازنه ليس ممنوعا من الصرف كأكلب وأبحر.",
     "en": "Because it is a loanword (dakhīl), and a loanword inclines toward what resembles it. “Ājur,” when arabicized in a lightened form, was not withheld from declension by assimilation to a parallel of the pattern afʿul used as a proper name — because not everything sharing its measure is barred from declension, as with aklub and abḥur."},

    # ---------------- Footnote 5 ----------------
    {"type": "note", "num": "٥"},
    {"type": "pair",
     "ar": "اعتذار عن أنه لم يعد الحمل على الموازن من الأسباب. وقد يعتذر عنه بأنه سبب على سبيل الاحتمال لا على القطع.",
     "en": "This is an excuse for his not counting assimilation to the parallel [pattern] among the causes [preventing declension]. One may also excuse it by [saying] that it is a cause by way of probability, not of certainty."},
    {"type": "pair",
     "ar": "قال المصنف في شرحه: يلزم هؤلاء أن يقولوا: الجمع وما أشبه الجمع. وقد قال بعضهم بذلك.",
     "en": "The author said in his commentary: these [scholars] are obliged to say “the plural and what resembles the plural,” and some of them have indeed said so."},

    # ---------------- Footnote 6 ----------------
    {"type": "note", "num": "٦"},
    {"type": "pair",
     "ar": "أي: قدر تقديرا.",
     "en": "That is: it was posited by supposition."},

    # ---------------- Footnote 7 ----------------
    {"type": "note", "num": "٧"},
    {"type": "pair",
     "ar": "هذه عبارة السيد إنما قال: «كأنه»؛ لأن السروالة لم تجيء بمعنى قطعة من السراويل، بل جاءت بمعنى قطعة الخرقة، فيكون المفرد كالجمع مفروضا.",
     "en": "This is the wording of al-Sayyid. He said only “as though,” because “sirwāla” has not come [in usage] with the meaning of a piece of the trousers, but rather with the meaning of a piece of cloth (khirqa); so the singular is, like the plural, [merely] supposed."},
    {"type": "pair",
     "ar": "وإنما لم يجعل جمعا لها بالمعنى الثاني حتى يكون المفرد متحققا؛ لأن السراويل مختص بالإزار، فلا يصح أن يكون السروالة بهذا المعنى مفردا له.",
     "en": "He did not make it [sarāwīl] a plural of it [sirwāla] in the second meaning — which would make the singular actual — because “sarāwīl” is specific to the waist-garment (izār); so it is not correct that “sirwāla” in this [second] meaning be a singular for it."},
    {"type": "pair",
     "ar": "ولقائل أن يقول: إن سراويل منقول من المعنى الجمعي إلى هذا الجنس، ولم يلاحظ فيه معنى الأقطاع أصلا، فجاز أن يكون منقولا إليه من معنى الأقطاع لا من أقطاع الإزار.",
     "en": "One might say: “sarāwīl” has been transferred from the plural sense to this generic [sense], and the notion of [multiple] pieces (aqṭāʿ) was not observed in it at all; so it is admissible that it was transferred to it from the notion of pieces [in general], not from the pieces of the waist-garment."},
    {"type": "pair",
     "ar": "إن قيل: نقل الجمع إلى الواحد في الأجناس لم يجيء، نعم جاء في الأشخاص كمدائن؟",
     "en": "If it be objected: the transfer of a plural to [denote] a single [thing] does not occur with generic terms; granted, it does occur with individuals (ashkhāṣ), as in “Madāʾin”?"},
    {"type": "pair",
     "ar": "أجيب: بأن ذلك في الجمع المحقق لا في مطلق الجمع، وبأن المفرد إذا اشتمل على الأقطاع جاز إطلاق اسم تلك الأقطاع عليه كما يقال: ثوب شراذم جمع شرذمة، وهي القطعة.",
     "en": "The reply is: that [restriction] applies to the actual plural, not to the plural absolutely; and [further,] that when a single [thing] comprises [several] pieces, it is admissible to apply the name of those pieces to it — as one says “a garment of shreds (sharādhim),” the plural of shirdhima, which is a piece."},
    {"type": "pair",
     "ar": "وفيه أن ذلك من باب إجراء الجمع على الواحد لا من باب إطلاق الجمع عليه، اللهم إلا أن يقال: إذا صح الإجراء صح الإطلاق.",
     "en": "But there is [an objection] in this: that this belongs to the category of predicating a plural of a single [thing], not to the category of applying the plural [as a name] to it — unless one says: if the predication is sound, the application is [also] sound."},
]
