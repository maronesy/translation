# -*- coding: utf-8 -*-
"""Mulla Jami — al-Fawāʾid al-Ḍiyāʾiyya. Source PDF page 514 (printed ٥١٣)."""

PAGE_NUMBER = 514
PRINTED_PAGE = "٥١٣"   # Arabic-Indic, as printed

BLOCKS = [
    # ---------------- The commentary text (matn) ----------------
    # Continues «بلا واسطة -كما» at the foot of PDF p. 513 (mid-sentence).
    {"type": "matn",
     "ar": "يجيء مثاله- أو بواسطة كما إذا كان قبل المضاف إلى ما فيه معنى الاستفهام نحو: «علمت غلام من أنت؟»",
     "en": "…its example will come — or through an intermediary, as when it is before what is annexed to something containing the sense of interrogation, as in “ʿalimtu ghulāmu man anta?” (I knew whose servant you are);"},
    {"type": "matn",
     "ar": "(و) قبل (النفي) الداخل على معموليها[[١]] (و) قبل (اللام) أي: لام الابتداء الداخلة على معموليها",
     "en": "(and) before (the negation) that enters upon its two governed terms, (and) before (the lām), that is, the lām of the inchoative (lām al-ibtidāʾ) that enters upon its two governed terms,"},
    {"type": "matn",
     "ar": "(مثل: «علمت أزيد عندك أم عمرو»؟) مثال للتعليق بالاستفهام، وترك مثال أخويه بالمقايسة،",
     "en": "(as in “ʿalimtu a-zaydun ʿindaka am ʿamrun?” (I knew whether Zayd is with you or ʿAmr)). It is an example of suspension (taʿlīq) by interrogation; he left out the example of its two sisters, [leaving them] to analogy."},
    {"type": "matn",
     "ar": "فمثال النفي: «علمت ما زيد في الدار»، ومثال اللام: «علمت لزيد منطلق»،",
     "en": "So the example of negation is “ʿalimtu mā zaydun fī al-dāri” (I knew that Zayd is not in the house), and the example of the lām is “ʿalimtu la-zaydun munṭaliqun” (I knew that Zayd is indeed departing)."},
    {"type": "matn",
     "ar": "وإنما تعلق قبل هذه الثلاثة؛ لأن هذه الثلاثة تقع في صدر الجملة وضعا[[٢]]، فاقتضت بقاء صورة الجملة،",
     "en": "They are suspended before these three only because these three occur, by their original assignment (waḍʿ), at the head of the sentence, and so they require that the form of the sentence be preserved;"},
    {"type": "matn",
     "ar": "وهذه الأفعال توجب تغييرها بنصب جزأيها، فوجب التوفيق باعتبار أحدهما لفظا والآخر معنى،",
     "en": "while these verbs require its alteration by putting its two parts in the accusative. So a reconciliation was necessary by taking one of them into account in wording and the other in meaning:"},
    {"type": "matn",
     "ar": "فمن حيث اللفظ[[٣]] روعي الاستفهام والنفي ولام الابتداء، ومن حيث المعنى روعيت هذه الأفعال،",
     "en": "with respect to wording, the interrogation, the negation and the lām of the inchoative are observed; and with respect to meaning, these verbs are observed."},
    {"type": "matn",
     "ar": "والتعليق مأخوذ من قولهم: «امرأة معلقة» أي: مفقودة الزوج، تكون كالشيء المعلق لا مع الزوج لفقدانه، ولا بلا زوج؛ لتجويزها وجوده، فلا تقدر على التزويج،",
     "en": "The term taʿlīq (suspension) is taken from their saying “imraʾa muʿallaqa” (a suspended woman), that is, one whose husband is missing: she is like a thing suspended, neither with a husband, since he is missing, nor without a husband, since she admits the possibility of his being alive, and so she is unable to marry."},
    {"type": "matn",
     "ar": "فالفعل المعلق ممنوع من العمل لفظا، عامل معنى وتقديرا؛ لأن معنى «علمت لزيد قائم»: علمت قيام زيد، كما كان كذلك عند انتصاب الجزأين،",
     "en": "So the suspended verb is prevented from governing in wording, [but] governs in meaning and by supposition; for the meaning of “ʿalimtu la-zaydun qāʾimun” is “I knew Zayd’s standing”, just as it is so when the two parts are in the accusative."},
    {"type": "matn",
     "ar": "ومن ثم جاز عطف الجملة المنصوبة جزآها على الجملة التعليقية نحو: «علمت لزيد قائم وبكرا قاعدا».",
     "en": "Hence it is permissible to coordinate a sentence whose two parts are in the accusative with the suspended sentence, as in “ʿalimtu la-zaydun qāʾimun wa-bakran qāʿidan” (I knew that Zayd is indeed standing and Bakr sitting)."},
    {"type": "matn",
     "ar": "والفرق[[٤]] بين الإلغاء والتعليق من وجهين:",
     "en": "The difference between cancellation (ilghāʾ) and suspension (taʿlīq) is in two respects:"},
    {"type": "matn",
     "ar": "أحدهما: أن الإلغاء جائز لا واجب، والتعليق واجب[[٥]].",
     "en": "The first: cancellation is permissible, not obligatory, while suspension is obligatory."},
    {"type": "matn",
     "ar": "والثاني: أن الإلغاء إبطال العمل في اللفظ والمعنى، والتعليق إبطال العمل في",
     "en": "The second: cancellation is the voiding of government in both wording and meaning, while suspension is the voiding of government in…"},

    {"type": "rule"},

    # ---------------- Footnote 1 ----------------
    {"type": "note", "num": "١"},
    {"type": "pair",
     "ar": "قيد النفي بالداخلة على المعمولين، وكذا لام الابتداء؛",
     "en": "He qualified the negation as that which enters upon the two governed terms, and likewise the lām of the inchoative;"},
    {"type": "pair",
     "ar": "لأنه إذا تقدم أحد الأشياء الثلاثة على المفعول الثاني فقد لا يوجب التعليق في الأول نحو: علمت زيدا من هو، أو ما قائم أو لقائم.",
     "en": "because when one of the three things precedes the second object, it may not require suspension with respect to the first, as in “ʿalimtu zaydan man huwa” (I knew Zayd, who he is), or “mā qāʾimun” or “la-qāʾimun”."},
    {"type": "pair",
     "ar": "وجوز بعضهم تعليقه عن المفعولين في هذه الصور أيضا.",
     "en": "Some permitted its suspension from both objects in these cases as well."},
    {"type": "pair",
     "ar": "وإنما لم يقيد الاستفهام بذلك؛ لأنه قد يكون المفعول الأول متضمنا للاستفهام.",
     "en": "He did not qualify the interrogation in this way only because the first object may itself contain the interrogation."},

    # ---------------- Footnote 2 ----------------
    {"type": "note", "num": "٢"},
    # REVIEW: printed «إن زيد لقائم» (nominative زيد after إن); transcribed as printed.
    {"type": "pair",
     "ar": "قيد بذلك؛ لأن لام الابتداء قد تدخل على الخبر نحو: إن زيد لقائم احترازا عن اجتماع التي للتأكيد، لكنه خلاف الوضع.",
     "en": "He qualified [it] by this because the lām of the inchoative sometimes enters upon the predicate, as in “inna zayd la-qāʾimun” (Zayd is indeed standing), to avoid the conjunction of the two [particles] that serve for emphasis; but that is contrary to its original assignment."},

    # ---------------- Footnote 3 ----------------
    {"type": "note", "num": "٣"},
    {"type": "pair",
     "ar": "ولا يجوز العكس؛ لأنه لا يعلم حينئذ أن المعنوي يكون عاملا أو لا.",
     "en": "The reverse is not permissible, because it would then not be known whether the notional [factor] governs or not."},

    # ---------------- Footnote 4 ----------------
    {"type": "note", "num": "٤"},
    {"type": "pair",
     "ar": "مع اشتراكهما في إبطال العمل.",
     "en": "Despite their sharing in the voiding of government."},
    {"type": "pair",
     "ar": "والمراد الإلغاء المذكور منها لتخرج الصور الواجبة المذكورة سابقا،",
     "en": "What is meant is the cancellation mentioned among them [i.e., among the properties], so that the obligatory cases mentioned earlier are excluded;"},
    {"type": "pair",
     "ar": "وأما الفرق بين مطلق الإلغاء والتعليق فبالوجه الثاني فقط.",
     "en": "as for the difference between cancellation in general and suspension, it lies in the second respect only."},

    # ---------------- Footnote 5 ----------------
    {"type": "note", "num": "٥"},
    {"type": "pair",
     "ar": "فيه بحث لأنه لو كان الإلغاء جائزا لكان في قوله: ومنها جواز الإلغاء استدراك.",
     "en": "There is a difficulty in this: if cancellation were [by definition] permissible, there would be redundancy in his words “and among them is the permissibility of cancellation”."},
    {"type": "pair",
     "ar": "ولما صح ما تقدم من أن الإلغاء واجب في الصورة المفصلة،",
     "en": "Nor would what preceded be correct, namely that cancellation is obligatory in the cases set out in detail."},
    {"type": "pair",
     "ar": "وغاية ما يمكن أن يقال: إنه لم يرد الفرق بين معنى الإلغاء والتعليق، بل أراد الفرق بين خصيصتي الإلغاء والتعليق في هذا الباب بأن الإلغاء جائز.",
     "en": "The most that can be said is that he did not intend the difference between the meaning of cancellation and of suspension, but rather the difference between the two properties of cancellation and suspension in this chapter, namely that cancellation is permissible."},
    {"type": "pair",
     "ar": "ولهذا قيده بالجواز والتعليق واجب.",
     "en": "For this reason he qualified it [cancellation] by permissibility, while suspension is obligatory."},
    {"type": "pair",
     "ar": "ولذا لم يقيده بالجواز، بل سياق الكلام فيه بحث يفيد الوجوب، فتدبر.",
     "en": "And therefore he did not qualify it [suspension] by permissibility; rather, the context of the discussion of it conveys obligation. So reflect."},
]
