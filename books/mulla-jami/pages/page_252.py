# -*- coding: utf-8 -*-
"""Mulla Jami — al-Fawāʾid al-Ḍiyāʾiyya. Source PDF page 252 (printed ٢٥١)."""

PAGE_NUMBER = 252
PRINTED_PAGE = "٢٥١"   # Arabic-Indic, as printed

BLOCKS = [
    # ---------------- The commentary text (matn) ----------------
    {"type": "matn",
     "ar": "(و«زيد في الدار قائما»[[١]]) مثال للفظي الملفوظ حكما[[٢]]،",
     "en": "(And “Zayd is in the house, standing”): an example of the verbal [kind] uttered virtually;"},
    {"type": "matn",
     "ar": "فإن فاعلية الضمير المستكن في الظرف إنما هي باعتبار لفظ هذا الكلام ومنطوقه من غير اعتبار معنى خارج عنه، والضمير المستكن ملفوظ حكما.",
     "en": "for the agency of the pronoun latent in the adverbial phrase (ẓarf) is only by consideration of the wording of this speech and its explicit expression, without regard to a meaning outside it; and the latent pronoun is virtually uttered."},
    {"type": "matn",
     "ar": "(و«هذا زيد قائما») مثال للمعنوي؛ لأن مفعولية «زيد»[[٣]] ليس باعتبار لفظ هذا الكلام ومنطوقه، بل باعتبار معنى الإشارة أو التنبيه[[٤]] المفهومين من لفظ «هذا».",
     "en": "(And “This is Zayd, standing”): an example of the semantic [kind]; for the objecthood of “Zayd” is not by consideration of the wording of this speech and its explicit expression, but by consideration of the meaning of pointing or of drawing attention (tanbīh), both understood from the word “hādhā.”"},
    {"type": "matn",
     "ar": "ولا شك أنهما ليسا مما يقصد المتكلم الإخبار بهما عن نفسه حتى يقدر في نظم الكلام «أشير» أو «أنبه» ويصير «زيد» به مفعولا لفظيا،",
     "en": "There is no doubt that these two are not among what the speaker intends to report about himself, such that “I point” or “I draw attention” would be supplied in the construction of the speech and “Zayd” would thereby become a verbal object;"},
    {"type": "matn",
     "ar": "بل مفعوليته إنما هي باعتبار معنى «أشير» أو «أنبه» الخارج عن منطوق الكلام المعتبر، لصحة وقوع القائم حالا، فهي معنوية لا لفظية.",
     "en": "rather, its objecthood is only by consideration of the meaning of “I point” or “I draw attention,” which lies outside the explicit expression of the speech and is taken into account so that “standing” may validly occur as a ḥāl; so it is semantic, not verbal."},
    {"type": "matn",
     "ar": "(وعاملها[[٥]]) أي: عامل الحال (إما الفعل) الملفوظ أو المقدر نحو: «ضربت زيدا قائما» و«زيد في الدار قائما» إن كان الظرف مقدرا بالفعل.",
     "en": "(Its governor), that is, the governor of the ḥāl, (is either the verb), uttered or implied, as in “I struck Zayd standing” and “Zayd is in the house, standing,” if the adverbial phrase is construed with an implied verb."},
    {"type": "matn",
     "ar": "(أو شبهه) وهو ما يعمل عمل الفعل، وهو من تركيبه[[٦]]:",
     "en": "(Or what resembles it), namely what governs as the verb governs and is formed from its letters:…"},

    {"type": "rule"},

    # ---------------- Footnote 1 ----------------
    {"type": "note", "num": "١"},
    {"type": "pair",
     "ar": "مثال اللفظي الملفوظ حكما.",
     "en": "An example of the verbal [kind] uttered virtually."},
    {"type": "pair",
     "ar": "هذا توجيه جيد لكن المصنف جعله في شرحه مثالا للفاعل المعنوي،",
     "en": "This is a good explanation; but the author made it, in his own commentary, an example of the semantic agent;"},
    {"type": "pair",
     "ar": "ويتجه عليه أن فاعل الظرف فاعل لفظي؛ لأن عامله مقدر في نظم الكلام،",
     "en": "and against him it is objected that the agent of the adverbial phrase is a verbal agent, because its governor is implied in the construction of the speech;"},
    {"type": "pair",
     "ar": "اللهم إلا أن يقال: إن اعتبار عامله لما لم يكن لضرورة المعنى كان في حكم المفهوم من الفحوى.",
     "en": "unless it be said that, since taking its governor into account is not due to the requirement of the meaning, it has the status of what is understood from the purport."},
    {"type": "pair",
     "ar": "ولا يجوز أن يقال: إن «قائما» حال عن «زيد» وهو مبتدأ لكنه فاعل معنى لاتحاده مع الضمير الذي هو فاعل الظرف؛",
     "en": "It may not be said that “qāʾiman” is a ḥāl of “Zayd,” which is a mubtadaʾ but an agent in meaning because it is one with the pronoun that is the agent of the adverbial phrase;"},
    {"type": "pair",
     "ar": "لأنه يلزم اختلاف عامل الحال وصاحبها، وذا لا يجوز عند الأكثرين على أنه لا يصير فاعلا معنويا على التفسير المذكور.",
     "en": "for that entails that the governor of the ḥāl and that of its owner differ, which is not permitted according to most; besides, it would not become a semantic agent on the explanation given."},

    # ---------------- Footnote 2 ----------------
    {"type": "note", "num": "٢"},
    {"type": "pair",
     "ar": "رد على ما في شرح المصنف أنه مثال للحال عن الفاعل معنى.",
     "en": "A rejection of what is in the author’s commentary, that it is an example of a ḥāl of an agent in meaning."},

    # ---------------- Footnote 3 ----------------
    {"type": "note", "num": "٣"},
    {"type": "pair",
     "ar": "الظاهر أنه إذا اعتبر العامل حرف التنبيه يكون ذو الحال اسم الإشارة لاتصالها به،",
     "en": "What appears is that if the governor is taken to be the particle of drawing attention [hā], the owner of the ḥāl is the demonstrative noun, because of its being joined to it;"},
    {"type": "pair",
     "ar": "بل الظاهر أن الإشارة المستنبطة منه أيضا عامل فيه؛ لأن الإشارة متعلقة بما يعبر عنه باسم الإشارة، وذكر «زيد» ليس لتعلق الإشارة به بل للحكم به، فتدبر.",
     "en": "indeed, what appears is that the pointing derived from it also governs it; for pointing attaches to what is expressed by the demonstrative noun, and “Zayd” is mentioned not because the pointing attaches to it but in order to predicate it. So reflect."},

    # ---------------- Footnote 4 ----------------
    {"type": "note", "num": "٤"},
    {"type": "pair",
     "ar": "الأول أولى لأن «زيدا» مشار إليه لا منبه عليه، فإن المنبه عليه حقيقة هو ذا زيد مع تقارب الاسم والفعل.",
     "en": "The first is preferable, because “Zayd” is what is pointed at, not what attention is drawn to; for what attention is drawn to in reality is “dhā Zayd,” given the closeness of the noun and the verb."},

    # ---------------- Footnote 5 ----------------
    {"type": "note", "num": "٥"},
    {"type": "pair",
     "ar": "فصل العامل ههنا لتحقيق لفظية الفاعل والمفعول ومعنويتهما،",
     "en": "He detailed the governor here to establish the verbal or semantic character of the agent and the object,"},
    # REVIEW: print reads «على الفظي» (for «اللفظي»); transcribed as printed.
    {"type": "pair",
     "ar": "وليكون توطئة لامتناع تقدم الحال على العامل المعنوي، وجواز تقدمها على الفظي المفهوم من تخصيص الامتناع به.",
     "en": "and as a preparation for the impossibility of the ḥāl preceding a semantic governor, and the permissibility of its preceding a verbal one, understood from restricting the impossibility to the former."},
    {"type": "pair",
     "ar": "وكأنه أراد ألا يفصل بين مباحث التقديم، وإلا لكان المناسب أن يذكر ما هو توطئة له عقب ذلك التفصيل.",
     "en": "It is as though he wished not to separate the discussions of preposing; otherwise it would have been fitting to mention what prepares for it right after that detailed treatment."},

    # ---------------- Footnote 6 ----------------
    {"type": "note", "num": "٦"},
    {"type": "pair",
     "ar": "أي: يشمل على حروف الفعل المفيد هو لمعناه. وحينئذ خرج اسم الفعل عن شبهه.",
     "en": "That is, it comprises the letters of the verb that conveys its meaning. In that case the verbal noun (ism al-fiʿl) is excluded from “what resembles it.”"},
    {"type": "pair",
     "ar": "ولا يخفى أنه لا يدخل في معنى الفعل على ما صرح به الشارح، فالأولى أن يفسر معنى الفعل بحيث يدخل فيه اسم الفعل.",
     "en": "It is not hidden that it does not enter into “the meaning of the verb” according to what the commentator stated explicitly; so it is preferable to explain “the meaning of the verb” in such a way that the verbal noun enters into it."},
]
