# -*- coding: utf-8 -*-
"""Mulla Jami — al-Fawāʾid al-Ḍiyāʾiyya. Source PDF page 369 (printed ٣٦٨)."""

PAGE_NUMBER = 369
PRINTED_PAGE = "٣٦٨"   # Arabic-Indic, as printed

BLOCKS = [
    # ---------------- The commentary text (matn) ----------------
    # Follows «…فههنا أيضا الأخفش تصرف في الضمير، وسيبويه في العامل.» at the foot of PDF p. 368 (new sentence).
    {"type": "matn",
     "ar": "(ونون الوقاية[[١]] مع الياء[[٢]]) أي: ياء المتكلم[[٣]] (لازمة في الماضي) إذا لحقه تلك الياء،",
     "en": "(The nūn of protection (nūn al-wiqāya) with the yāʾ), that is, the yāʾ of the speaker, (is required in the perfect) when that yāʾ is attached to it,"},
    {"type": "matn",
     "ar": "لتقي آخر الماضي عن الكسرة المختصة بالاسم التي هي أخت الجر[[٤]]، ولهذا سميت نون الوقاية[[٥]] نحو: «ضربني»",
     "en": "to protect the end of the perfect from the kasra that is peculiar to the noun, the sister of the genitive; this is why it is called the nūn of protection; as in “ḍarabanī” (he struck me)."},
    {"type": "matn",
     "ar": "(و) كذلك نون الوقاية لازمة (في المضارع) لكن لا مطلقا، بل حال كونه (عريا عن نون الإعراب[[٦]]) أي: عن نون هي الإعراب، نحو: «يضربني»",
     "en": "(And) likewise the nūn of protection is required (in the imperfect), though not absolutely, but only when it is (free of the nūn of inflection), that is, of a nūn that is the inflection, as in “yaḍribunī” (he strikes me),"},
    # REVIEW: «أخر» is printed with hamza (expected «آخر»); transcribed as printed.
    {"type": "matn",
     "ar": "لتقي أخر المضارع أيضا عن تلك الكسرة، بخلاف كسرة «تضربين»؛ لأنها في الوسط حكما[[٧]]،",
     "en": "to protect the end of the imperfect also from that kasra; unlike the kasra of “taḍribīna”, because it is medial in status,"},
    {"type": "matn",
     "ar": "وبخلاف كسرة ﴿لم يكن الذين كفروا﴾[[٨]]، ﴿وقل الحق﴾[[٩]] لعروضها[[١٠]].",
     "en": "and unlike the kasra of “lam yakuni lladhīna kafarū” (Those who disbelieved were not…) and “wa-quli l-ḥaqqu” (And say: the truth…), because it is incidental."},
    {"type": "matn",
     "ar": "(وأنت مع النون) الإعرابية الكائنة (فيه) أي: في المضارع (و) مع («لدن» و«إن» وأخواتها) يعني: «أن وكأن ولكن وليت[[١١]] ولعل»",
     "en": "(With the nūn) of inflection that is (in it), that is, in the imperfect, (and) with (“ladun” and “inna” and its sisters), meaning “anna”, “kaʾanna”, “lākinna”, “layta” and “laʿalla”, you"},
    {"type": "matn",
     "ar": "(مخير) بين الإتيان بنون الوقاية للمحافظة على الحركات البنائية[[١٢]] في غير «لدن» وعلى السكون في «لدن» وبين",
     "en": "(have the choice) between using the nūn of protection, to preserve the indeclinable vowels in words other than “ladun” and the quiescence in “ladun”, and…"},

    {"type": "rule"},

    # ---------------- Footnote 1 ----------------
    {"type": "note", "num": "١"},
    {"type": "pair",
     "ar": "وتسمى أيضا نون العماد؛ لأن العماد كما يحفظ السقف عن السقوط يحفظ ذلك النون آخر الكلمة عن الكسر.",
     "en": "It is also called the nūn of support (nūn al-ʿimād), because just as a pillar keeps a roof from falling, that nūn keeps the end of the word from the kasra."},

    # ---------------- Footnote 2 ----------------
    {"type": "note", "num": "٢"},
    {"type": "pair",
     "ar": "نون الوقاية مبتدأ مع الياء خبره لازمة حال من ضمير الظرف.",
     "en": "“Nūn al-wiqāya” is the subject; “maʿa al-yāʾ” is its predicate; “lāzimatun” is a circumstantial from the pronoun in the adverbial."},
    {"type": "pair",
     "ar": "وقوله: وأنت مع النون إلى آخره. وقوله: ويختار في «ليت» إلى آخره وعكسها، «لعل» حمل معطوفات على الحال.",
     "en": "His words “wa-anta maʿa al-nūn…” and his words “and in “layta” … is preferred” and its converse, “laʿalla”, are taken as conjuncts to the circumstantial."},
    {"type": "pair",
     "ar": "وقوله: ويختار مستثنى من التخيير، وكذا عكسها «لعل» أو قرينة على أن المراد بأخوات «أن» ما عدا «ليت ولعل».",
     "en": "His words “is preferred” are excepted from the choice, as is its converse, “laʿalla”; or they are an indication that what is meant by the sisters of “anna” is those other than “layta” and “laʿalla”."},

    # ---------------- Footnote 3 ----------------
    {"type": "note", "num": "٣"},
    {"type": "pair",
     "ar": "إذ لم يعهد غيره.",
     "en": "Since no other [yāʾ] is known [here]."},

    # ---------------- Footnote 4 ----------------
    {"type": "note", "num": "٤"},
    {"type": "pair",
     "ar": "وهي كسرة تكون في آخر الكلمة لا مطلق الكسرة.",
     "en": "That is, a kasra at the end of the word, not kasra in general."},
    {"type": "pair",
     "ar": "ولذا لم يتحاش عن كسرة نون الوقاية مع أن الحرف أيضا يجب أن يصان عن أخت الكسرة؛ لأنها لكونها على حرف واحد ليس كسرتها أخت الجر.",
     "en": "Hence the kasra of the nūn of protection was not avoided, although a particle too must be guarded from the sister of the kasra; for, consisting of a single letter, its kasra is not the sister of the genitive."},
    {"type": "pair",
     "ar": "ومن ههنا ظهر أنه لو قال: لتقي الماضي عن الكسرة إلى آخره لتم وإن ذكر الآخر مما لا يحتاج إليه.",
     "en": "From this it appears that had he said “to protect the perfect from the kasra” and so on, it would have been complete, and that the mention of “the end” is unnecessary."},

    # ---------------- Footnote 5 ----------------
    {"type": "note", "num": "٥"},
    {"type": "pair",
     "ar": "أي: نون هي سبب الوقاية، أو نون هي للوقاية تأمل.",
     "en": "That is, a nūn that is the cause of protection, or a nūn that is for protection. Reflect."},

    # ---------------- Footnote 6 ----------------
    {"type": "note", "num": "٦"},
    {"type": "pair",
     "ar": "سواء كان معه نون الضمير ونونا التأكيد، أو لم يكن معه أحدهما.",
     "en": "Whether the nūn of the pronoun and the two nūns of emphasis are with it, or neither of them is with it."},
    {"type": "pair",
     "ar": "وإنما جاز قيام نون الإعراب مقام نون الوقاية دون تلك النونات؛ لأن نون الإعراب كنون الوقاية، في أن لا معنى لها.",
     "en": "The nūn of inflection may stand in place of the nūn of protection, unlike those [other] nūns, only because the nūn of inflection is like the nūn of protection in having no meaning."},

    # ---------------- Footnote 7 ----------------
    {"type": "note", "num": "٧"},
    {"type": "pair",
     "ar": "لشدة امتزاج ياء الضمير فيه؛ لأنه فاعل بخلاف ياء المتكلم؛ لأنه مفعول، ولكونه علامة الإعراب تعد الياء المتأخر منه.",
     "en": "Because of how closely the pronominal yāʾ is fused into it, being an agent, unlike the yāʾ of the speaker, which is an object; and because [the nūn] is the sign of inflection, the yāʾ is counted as coming after it."},

    # ---------------- Footnote 8 ----------------
    {"type": "note", "num": "٨"},
    {"type": "pair",
     "ar": "سورة البينة: ١.",
     "en": "Qurʾān, Sūrat al-Bayyina 98:1."},

    # ---------------- Footnote 9 ----------------
    {"type": "note", "num": "٩"},
    {"type": "pair",
     "ar": "سورة الكهف: ٢٩.",
     "en": "Qurʾān, Sūrat al-Kahf 18:29."},

    # ---------------- Footnote 10 ----------------
    {"type": "note", "num": "١٠"},
    {"type": "pair",
     "ar": "لا يخفى أن العروض مشترك بينه وبين ما قبل الياء، وأنه يقوي مماثلتها للجر،",
     "en": "It is not hidden that incidentality is shared between this and what precedes the yāʾ, and that it strengthens its resemblance to the genitive;"},
    {"type": "pair",
     "ar": "فالأولى الإعراض عنه، والتمسك بأنه كالسكون حيث لم يعد معها المحذوف لالتقاء الساكنين.",
     "en": "so it is better to set it aside and hold rather that it is like quiescence, since with it what was elided for the meeting of two quiescent letters is not restored."},

    # ---------------- Footnote 11 ----------------
    {"type": "note", "num": "١١"},
    {"type": "pair",
     "ar": "لا يخير في «ليت ولعل»؛ لأنه عبارة عن مساواة الأمرين بخلاف الاختيار، فالأولى أن «ليت ولعل» مستثنيان عنها.",
     "en": "There is no choice with “layta” and “laʿalla”, because choice means the two options are equal, unlike preference; so it is better [to say] that “layta” and “laʿalla” are excepted from them."},

    # ---------------- Footnote 12 ----------------
    {"type": "note", "num": "١٢"},
    {"type": "pair",
     "ar": "هذا ظاهر في غير التثنية. وأما في التثنية، فوجهه أن كسرة المناسبة مغايرة لكسرة نون الإعراب، أو أنها لطرد الباب.",
     "en": "This is evident outside the dual. In the dual, the reason is that the kasra of harmony differs from the kasra of the nūn of inflection, or that it is for the consistency of the rule."},
]
