# -*- coding: utf-8 -*-
"""Mulla Jami — al-Fawāʾid al-Ḍiyāʾiyya. Source PDF page 35 (printed ٣٤)."""

PAGE_NUMBER = 35
PRINTED_PAGE = "٣٤"   # Arabic-Indic, as printed

BLOCKS = [
    # ---------------- The base text (matn) ----------------
    {"type": "matn",
     "ar": "أحكام اللفظ[[١]]، فكان[[٢]] لفظا حكما لا حقيقة[[٣]].",
     "en": "the rulings of the utterance, so it became an utterance by [legal] status (ḥukman), not in reality (ḥaqīqatan)."},
    {"type": "matn",
     "ar": "والمحذوف لفظ حقيقة[[٤]]؛ لأنه[[٥]] قد يتلفظ به الإنسان في بعض الأحيان[[٦]].",
     "en": "The elided [word] (al-maḥdhūf) is an utterance in reality, because a human being does at times articulate it."},
    {"type": "matn",
     "ar": "وكلمات الله تعالى داخلة فيه[[٧]]؛ إذ هي[[٨]] مما يتلفظ به الإنسان[[٩]].",
     "en": "The words (kalimāt) of Allah, the Exalted, fall under it, since they are among what a human being articulates."},
    {"type": "matn",
     "ar": "وعلى هذا القياس كلمات الملائكة، والجن[[١٠]]، والدوال الأربع[[١١]] -وهي الخطوط، والعقود، والإشارات، والنصب[[١٢]]- غير داخلة في اللفظ[[١٣]]، فلا حاجة إلى",
     "en": "By the same analogy, the words of the angels and of the jinn, and the four indicators (al-dawāll al-arbaʿ) — namely written marks (khuṭūṭ), knot-reckoning (ʿuqūd), gestures (ishārāt), and signposts (nuṣab) — are not included in [the term] “utterance”; so there is no need for"},

    {"type": "rule"},

    # ---------------- Footnote 1 ----------------
    {"type": "note", "num": "١"},
    {"type": "pair",
     "ar": "من كونه مسندا إليه، ومعطوفا عليه، وذا حال، وغير ذلك.",
     "en": "[The rulings] of its being that to which predication is made (musnad ilayhi), that upon which conjunction is made (maʿṭūf ʿalayhi), a possessor of a circumstantial state (dhū ḥāl), and so forth."},

    # ---------------- Footnote 2 ----------------
    {"type": "note", "num": "٢"},
    {"type": "pair",
     "ar": "ذلك المنوي.",
     "en": "[That is:] that implied [pronoun]."},

    # ---------------- Footnote 3 ----------------
    {"type": "note", "num": "٣"},
    {"type": "pair",
     "ar": "تفريع على الدليلين. والمناسب أن يقال: فلم يكن لفظا حقيقة، بل حكما، تفريعا على الدليل الأول، والثاني على الثاني بطريق اللف والنشر المرتب.",
     "en": "A derivation (tafrīʿ) upon the two proofs. The fitting [wording] would be to say: “so it is not an utterance in reality, but rather by status,” as a derivation upon the first proof, and the second [clause] upon the second [proof], by way of ordered distribution (al-laff wa-l-nashr al-murattab)."},
    {"type": "pair",
     "ar": "لكنه اختار هذا الطريق إشارة إلى أن المقصود الأصلي إثبات كون المنوي لفظا حكما، ونفي حقيقته طفيلي لإثبات ذلك، فتأمل، أو يجعل التفريع عقيب المفرع عليه ويليه بقدر الإمكان.",
     "en": "But he chose this path to indicate that the primary aim is establishing that the implied [pronoun] is an utterance by status, while negating its being one in reality is subordinate (ṭufaylī) to establishing that — so ponder. Or [it may be that] the derivation is placed immediately after that from which it is derived, and follows it as far as possible."},

    # ---------------- Footnote 4 ----------------
    {"type": "note", "num": "٤"},
    {"type": "pair",
     "ar": "لما أشار إلى أن اللفظ حقيقي وحكمي، أراد أن يبين أن المحذوف من القسم الأول دون القسم الثاني.",
     "en": "When he indicated that the utterance is [of two kinds,] real and constructive, he wished to make clear that the elided belongs to the first kind, not the second."},
    {"type": "pair",
     "ar": "ويمكن أن يكون هذه العبارة مع ما سبق من قوله: «واللفظ الحكمي كالمنوي» إشارة إلى رد ما نقل عن المصنف أنه قال في إيضاح المفصل: المستتر هو المحذوف، لكن عبروا عن المحذوف الذي هو الفاعل بالمستكن صونا للسان عن حذف الفاعل.",
     "en": "It may also be that this expression, together with what preceded of his statement “the constructive utterance is like the implied [pronoun],” is an indication of a refutation of what was transmitted from the author — that he said in Īḍāḥ al-Mufaṣṣal: “the hidden [pronoun] (al-mustatir) is the elided (al-maḥdhūf), but they expressed the elided — which is the agent — by [the term] ‘concealed’ (al-mustakinn), to guard the tongue from [saying] ‘elision of the agent.’”"},
    {"type": "pair",
     "ar": "وجه الرد: أن التحقيق أن المستتر لفظ حكمي، فلو كان محذوفا لكان حقيقة، ولم يتحقق اللفظ الحكمي، فيرد، فلا يحتاج إلى تعميم ما يتلفظ به الإنسان من الحقيقي والحكمي.",
     "en": "The manner of the refutation: the sound view is that the hidden [pronoun] is a constructive utterance; so were it elided, it would be [an utterance] in reality, and the constructive utterance would not be realized — so [the objection] stands answered — and hence there is no need to generalize “what a human articulates” to [include] both the real and the constructive."},

    # ---------------- Footnote 5 ----------------
    {"type": "note", "num": "٥"},
    {"type": "pair",
     "ar": "أي: لأن المحذوف كذلك.",
     "en": "That is: because the elided is likewise [something a human articulates]."},

    # ---------------- Footnote 6 ----------------
    {"type": "note", "num": "٦"},
    {"type": "pair",
     "ar": "أي: في غير هذا التركيب الذي حذف «هو» فيه.",
     "en": "That is: in a construction other than this one, in which “huwa” was elided."},

    # ---------------- Footnote 7 ----------------
    {"type": "note", "num": "٧"},
    {"type": "pair",
     "ar": "أي: في اللفظ بمقتضى هذا التعريف؛ لأنها مما يتلفظ به الإنسان في بعض الأحيان، وإن كانت بالقياس إليه سبحانه لا يصدق عليها؛ إذ من شأنه أن يتلفظ بها الإنسان، أو لأنها مما يتلفظ بها حكما كالمنويات.",
     "en": "That is: [they fall] within [the term] “utterance” by the requirement of this definition, because they are among what a human articulates at times — even if, in relation to Him, Glorified is He, [the description] does not [truly] apply to them; for it is of [the utterance’s] nature that a human articulate it — or because they are among what is articulated by [legal] status, like the implied [pronouns] (al-manwiyyāt)."},

    # ---------------- Footnote 8 ----------------
    {"type": "note", "num": "٨"},
    {"type": "pair",
     "ar": "أي: الكلمة اللفظية المكتوبة في المصاحف.",
     "en": "That is: the verbal word (al-kalima al-lafẓiyya) written in the copies of the Muṣḥaf."},

    # ---------------- Footnote 9 ----------------
    {"type": "note", "num": "٩"},
    {"type": "pair",
     "ar": "أي: إذ هي مما يتلفظ به الإنسان إما بالفعل أو من شأنه أن يتلفظ به. وكل ما هو كذلك فهو لفظ يرد عليه أن كون جميع كلمات الله تعالى كذلك ممنوع.",
     "en": "That is: since they are among what a human articulates, either in actuality or such that it is of its nature to be articulated. And everything that is thus is an utterance — against which it is objected that [the claim] that all the words of Allah, the Exalted, are likewise is disallowed."},

    # ---------------- Footnote 10 ----------------
    {"type": "note", "num": "١٠"},
    {"type": "pair",
     "ar": "لا يقال على الوجهين الأولين: إن ما يتلفظ به الإنسان مغاير بالشخص لما تكلم به الحق سبحانه، فكيف يصح صدق ما ذكر عليها؟ لأنا نقول: هذا تدقيق فلسفي غير ملتفت عند الأدباء، فإن اختلاف المحل عندهم كاختلاف المكان.",
     "en": "One should not say, regarding the first two considerations: that what a human articulates is distinct in individual identity (bi-l-shakhṣ) from what the Real, Glorified is He, has uttered — so how can the aforesaid [description] be truly predicated of them? For we say: this is a philosophical subtlety to which the litterateurs (udabāʾ) pay no heed, since with them difference of locus is like difference of place."},
    {"type": "pair",
     "ar": "ثم لا يخفى أن هذا الاعتذار إنما يحتاج إليه إذا ثبت أن لكلمات الله سبحانه قياما به، وهو يخالف ما عليه المحققون، أو نقض بما في علمه من الكلمات، أو بما يظهر في غير الإنسان.",
     "en": "Then it is not hidden that this excuse is needed only if it is established that the words of Allah, Glorified is He, have a subsistence in Him (qiyāman bihi) — which contradicts what the verifying scholars (muḥaqqiqūn) hold — or [if it is] refuted by what is in His knowledge of the words, or by what appears in [beings] other than the human."},

    # ---------------- Footnote 11 ----------------
    {"type": "note", "num": "١١"},
    {"type": "pair",
     "ar": "وكذا أمثالها، مثل: «ضرب»: النقارة الدالة على ركوب السلطان.",
     "en": "And likewise their similars — such as “ḍarb”: the drum-beat (naqāra) that signals the riding-out of the ruler."},

    # ---------------- Footnote 12 ----------------
    {"type": "note", "num": "١٢"},
    {"type": "pair",
     "ar": "جمع نصبة، وهي ما وضع لتعيين المسافة أو الطريق، كذا قال الفاضل المحشي. فلم يتناول للعلم الدال على التعبير المشترك، فهو أيضا من أمثالها.",
     "en": "The plural of nuṣba, which is that which is set up to mark out a distance or a road; thus said the eminent glossator (al-fāḍil al-muḥashshī). So it does not comprehend the marker (ʿalam) that indicates by shared expression; hence that too is among its likes."},

    # ---------------- Footnote 13 ----------------
    {"type": "note", "num": "١٣"},
    {"type": "pair",
     "ar": "الذي هو أول أجزاء التعريف. ولما لم تدخل في التعريف لم يحتج في تصحيح التعريف إلى اعتبار إخراجها بقيد حتى يلزمنا ارتكاب تعسف.",
     "en": "[The “utterance”] which is the first component of the definition. Since [these four indicators] do not enter into the definition, there is no need, in order to make the definition sound, to consider excluding them by a restriction — so that we would be compelled to commit a forced construal (taʿassuf)."},
    {"type": "pair",
     "ar": "كما تعسفوا قالوا: إن الجنس والفصل إذا كان بينهما عموم من وجه جاز الاحتراز بالجنس، لجواز أن يعتبر الفصل جنسا والجنس فصلا.",
     "en": "As they committed [a forced construal when] they said: if between the genus and the differentia there is [only] partial overlap (ʿumūm min wajh), then guarding [against something] by the genus is permissible, since it is possible to regard the differentia as a genus and the genus as a differentia."},
]
