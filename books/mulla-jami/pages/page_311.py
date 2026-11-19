# -*- coding: utf-8 -*-
"""Mulla Jami — al-Fawāʾid al-Ḍiyāʾiyya. Source PDF page 311 (printed ٣١٠)."""

PAGE_NUMBER = 311
PRINTED_PAGE = "٣١٠"   # Arabic-Indic, as printed

BLOCKS = [
    # ---------------- The commentary text (matn) ----------------
    # Continues «… بأن يسقط بعض المعاني عن ملاحظة» at the foot of PDF p. 310.
    {"type": "matn",
     "ar": "العقل بإزاء ما يسقط من اللفظ، بل المعنى على ما كان عليه قبل الإضافة والتخفيف اللفظي.",
     "en": "…of the intellect corresponding to what drops from the wording; rather, the meaning remains as it was before the annexation and the lightening of the wording."},
    {"type": "matn",
     "ar": "أما في لفظ المضاف فقط بحذف التنوين حقيقة مثل: «ضارب زيد»، أو حكما مثل: «حواج بيت الله»، أو بحذف نوني التثنية والجمع مثل: «ضاربا زيد، وضاربو زيد».",
     "en": "[The lightening is] either in the wording of the annexed term alone, by dropping the tanwīn, actually, as in “ḍāribu Zaydin” (the one beating Zayd), or virtually, as in “ḥawājji bayti llāh” (the pilgrims to the House of Allah); or by dropping the nūn of the dual and of the plural, as in “ḍāribā Zaydin” and “ḍāribū Zaydin.”"},
    {"type": "matn",
     "ar": "وأما في لفظ المضاف إليه فقط بحذف الضمير واستتاره في الصفة كـ«القائم الغلام» كان أصله: «القائم غلامه»،",
     "en": "Or in the wording of the annexing term alone, by dropping the pronoun and its being concealed in the adjective, as in “al-qāʾim al-ghulām” (the one whose slave is standing), whose original form was “al-qāʾim ghulāmuhu”;"},
    {"type": "matn",
     "ar": "حذف الضمير من «غلامه» واستتر في «القائم»، وأضيف «القائم» إليه للتخفيف في المضاف إليه فقط.",
     "en": "the pronoun was dropped from “ghulāmuhu” and concealed in “al-qāʾim,” and “al-qāʾim” was annexed to it, for lightening in the annexing term alone."},
    {"type": "matn",
     "ar": "وأما في المضاف والمضاف إليه معا نحو: «زيد قائم الغلام»، أصله: «زيد قائم غلامه»[[١]]، فالتخفيف في المضاف بحذف التنوين وفي المضاف إليه بحذف الضمير واستتاره في الصفة.",
     "en": "Or in both the annexed and the annexing terms together, as in “Zayd is qāʾim al-ghulām,” whose original form is “Zayd is qāʾimun ghulāmuhu” (Zayd, his slave is standing); the lightening in the annexed term is by dropping the tanwīn, and in the annexing term by dropping the pronoun and its being concealed in the adjective."},
    {"type": "matn",
     "ar": "(ومن ثمة) أي: ومن جهة وجوب إفادة الإضافة اللفظية التخفيف، وانتفاء كل واحد من التعريف والتخصيص",
     "en": "(Hence), that is, because the formal genitive construction must convey lightening, and because both definiteness and specification are absent from it,"},
    {"type": "matn",
     "ar": "(جاز) تركيب («مررت برجل حسن الوجه») بإضافة الصفة إلى معمولها وجعلها صفة للنكرة،",
     "en": "(it was permissible) to construct (“I passed by a man fair of face”), by annexing the adjective to what it governs and making it an adjective of an indefinite noun;"},
    {"type": "matn",
     "ar": "فمن جهة أنها لم تفد تعريفا جاز هذا التركيب،",
     "en": "because it does not convey definiteness, this construction was permissible;"},
    {"type": "matn",
     "ar": "(وامتنع) تركيب («مررت بزيد حسن الوجه») فلو أفادت تعريفا لم يجز الأول للزوم كون المعرفة صفة للنكرة، ولجاز الثاني لكون المعرفة إذن صفة للمعرفة.",
     "en": "(and it was impossible) to construct (“I passed by Zayd fair of face”). Had it conveyed definiteness, the first would not have been permissible, since it would entail a definite noun qualifying an indefinite one; and the second would have been permissible, since a definite noun would then be qualifying a definite one."},
    # REVIEW: the matn has «ومن ثمة», but this sentence prints «بـ«ثم»»; transcribed as printed.
    {"type": "matn",
     "ar": "والمراد أن المشار إليه بـ«ثم»[[٢]] وهو مجموع أمور ثلاثة:",
     "en": "What is meant is that what “thamma” points to is the sum of three things:"},
    {"type": "matn",
     "ar": "١- وجوب إفادة الإضافة اللفظية التخفيف.",
     "en": "1. That the formal genitive construction must convey lightening."},

    {"type": "rule"},

    # ---------------- Footnote ٥ of PDF p. 310, continued ----------------
    {"type": "note", "num": ""},
    {"type": "pair",
     "ar": "وثانيهما: أنه يجعل الحصر بظاهره مضافا إلى خفة المعنى، أي: لا تفيد إلا تخفيفا في اللفظ لا في المعنى، فلا تفيد تعريفا ولا تخصيصا",
     "en": "The second: on its face, it makes the restriction relate to lightness of meaning, that is: “it conveys only lightening in the wording, not in the meaning,” so it conveys neither definiteness nor specification."},
    {"type": "pair",
     "ar": "فما يقال: إن ذكره في اللفظ للإشارة إلى وجه التسمية أقرب منه وإن كان بعيدا،",
     "en": "So what is said, that his mentioning “in the wording” is to indicate the reason for the name, is closer than this, even if it is far-fetched."},
    {"type": "pair",
     "ar": "فلعل الأقرب أن يقال: ولو قال: لا تفيد إلا تخفيفا لتبادر الذهن إلى تخفيف في المضاف على قياس إفادة الإضافة المعنوية التعريف أو التخصيص في المضاف،",
     "en": "Perhaps the closest is to say: had he said “it conveys only lightening,” the mind would have jumped to a lightening in the annexed term, on the analogy of the semantic construction’s conveying definiteness or specification in the annexed term;"},
    {"type": "pair",
     "ar": "فصرح بقوله: في اللفظ أي: في لفظ المتكلم سواء كان مضافا أو مضافا إليه للتعميم.",
     "en": "so he stated explicitly “in the wording,” that is, in the speaker’s wording, whether it be the annexed or the annexing term, so as to generalize."},

    # ---------------- Footnote 1 ----------------
    {"type": "note", "num": "١"},
    {"type": "pair",
     "ar": "لا يخفى عليك أن هذا الوجه لا يتم إلا على مذهب من لا يجوز القائم غلامه،",
     "en": "It will not be hidden from you that this explanation holds only on the doctrine of those who do not permit “al-qāʾim ghulāmuhu”;"},
    {"type": "pair",
     "ar": "وأنه لا تخفيف في المضاف إليه إلا بتبديل حرف متحرك بحرف ساكن؛ لأنه جاء حرف التعريف في المضاف إليه بعد حذف هاء الضمير.",
     "en": "and that there is no lightening in the annexing term except by replacing a vowelled letter with a quiescent one, since the definite article came into the annexing term after the hāʾ of the pronoun was dropped."},

    # ---------------- Footnote 2 ----------------
    {"type": "note", "num": "٢"},
    {"type": "pair",
     "ar": "قيل: لا يخفى أن هذه العبارة إنما يذكر لبناء لاحق على سابق وإثبات سابق بلاحق،",
     "en": "It has been said: it is evident that this expression is used only to base what follows on what precedes and to establish what precedes by what follows;"},
    {"type": "pair",
     "ar": "ولا يثبت لمجموع هنا بما ذكره، إذ لا يثبت عدم إفادة التخصيص. ويمكن أن يقال: عدم إفادة التعريف يستلزم عدم",
     "en": "and the sum here is not established by what he mentioned, since the absence of conveying specification is not established. It may be said: the absence of conveying definiteness entails the absence…"},
]
