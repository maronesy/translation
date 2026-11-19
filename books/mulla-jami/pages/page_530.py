# -*- coding: utf-8 -*-
"""Mulla Jami — al-Fawāʾid al-Ḍiyāʾiyya. Source PDF page 530 (printed ٥٢٩)."""

PAGE_NUMBER = 530
PRINTED_PAGE = "٥٢٩"   # Arabic-Indic, as printed

BLOCKS = [
    # ---------------- The commentary text (matn) ----------------
    {"type": "matn",
     "ar": "(وقد تدخل «أن») على خبر «كاد» تشبيها له بـ«عسى»[[١]] كما أنه يحذف «أن» عن خبر «عسى» تشبيها له بـ«كاد»، كقولهم:",
     "en": "(And “an” sometimes enters) upon the predicate of “kāda”, likening it to “ʿasā”, just as “an” is omitted from the predicate of “ʿasā”, likening it to “kāda”, as in their saying:"},
    {"type": "verse",
     "ar": "..............          قد كاد من طول البلى أن يمصحا[[٢]]",
     "en": "… it had nearly, from long wear, come to be effaced (an yamṣaḥā)."},
    {"type": "matn",
     "ar": "فلما كان كل واحد منهما مشابها للآخر، أعطي لكل واحد منهما حكم الآخر من وجه.",
     "en": "Since each of the two resembles the other, each of them was given the rule of the other in one respect."},
    {"type": "matn",
     "ar": "(وإذا دخل النفي على «كاد»، فهو) أي: «كاد» (كالأفعال) أي: كسائر الأفعال[[٣]] في إفادة أدوات النفي نفي مضمونها (على) القول (الأصح) ماضيا كان أو مستقبلا.",
     "en": "(And when negation enters upon “kāda”, it), that is, “kāda”, (is like the verbs), that is, like the rest of the verbs, in that the particles of negation convey the negation of its content, (according to the soundest) view, whether it is past or future."},
    {"type": "matn",
     "ar": "(وقيل نفيه) أي: نفي «كاد» (يكون للإثبات مطلقا) ماضيا كان أو مستقبلا،",
     "en": "(And it has been said that its negation), that is, the negation of “kāda”, (is for affirmation absolutely), whether it is past or future."},
    {"type": "matn",
     "ar": "أما في الماضي، فكقوله تعالى: ﴿وما كادوا يفعلون﴾[[٤]]، فإن المراد إثبات الفعل لا نفيه، بدليل: ﴿فذبحوها[[٥]]﴾[[٦]].",
     "en": "As for the past, it is as in His words, the Exalted: “and they nearly did not do it” (wa-mā kādū yafʿalūn); for what is meant is the affirmation of the act, not its negation, as is proved by “so they slaughtered her” (fa-dhabaḥūhā)."},
    {"type": "matn",
     "ar": "وأما المضارع، فلتخطئة الشعراء قول ذي الرمة.",
     "en": "As for the muḍāriʿ, [it is shown] by the poets’ faulting the words of Dhū al-Rumma:"},
    {"type": "verse",
     "ar": "......... لم يكد          رسيس الهوى من حب مية يبرح",
     "en": "… the first touch of passion from love of Mayya has scarcely (lam yakad) departed."},
    {"type": "matn",
     "ar": "بأنه يدل على زوال رسيس الهوى ولتسليمه تخطئتهم وتغييره قوله: «لم يكد» بقوله: «لم أجد»،",
     "en": "[faulting it] on the ground that it indicates the departure of the first touch of passion; and by his accepting their faulting and changing his words “lam yakad” to “lam ajid” (I have not found);"},
    # REVIEW: printed «لتخطئتم» (without the hā’ of «لتخطئتهم» as earlier in the sentence). Transcribed as printed.
    {"type": "matn",
     "ar": "فلولا كان نفي «كاد» للإثبات لما خطأه لما غيره لتخطئتم.",
     "en": "for were the negation of “kāda” not for affirmation, they would not have faulted him, nor would he have changed it because of their faulting."},
    {"type": "matn",
     "ar": "وأجيب عن الأول: بأن قوله تعالى: ﴿وما كادوا يفعلون﴾[[٧]] يدل على انتفاء الذبح وانتفاء القرب منه في وقت ما،",
     "en": "The first [argument] was answered thus: His words, the Exalted, “and they nearly did not do it” indicate the absence of the slaughter and the absence of nearness to it at some time,"},
    {"type": "matn",
     "ar": "وقوله: ﴿فذبحوها﴾[[٨]] قرينة تدل على ثبوت الذبح بعد انتفائه وانتفاء القرب منه، ولا تناقض بين انتفاء الشيء في وقت وثبوته في وقت آخر.",
     "en": "while His words “so they slaughtered her” are a contextual indication (qarīna) of the occurrence of the slaughter after its absence and the absence of nearness to it; and there is no contradiction between a thing’s absence at one time and its occurrence at another."},

    {"type": "rule"},

    # ---------------- Footnote 1 ----------------
    {"type": "note", "num": "١"},
    {"type": "pair",
     "ar": "عند من قال هو خبر. وأما عند الكوفيين فيقدر «أن» بدلا من الفاعل.",
     "en": "According to those who say it is a predicate. As for the Kūfans, “an” is construed as a substitute (badal) for the agent."},

    # ---------------- Footnote 2 ----------------
    {"type": "note", "num": "٢"},
    {"type": "pair",
     "ar": "مصح بمعنى: ذهب وانقطع.",
     "en": "Maṣaḥa means: it went away and ceased."},

    # ---------------- Footnote 3 ----------------
    {"type": "note", "num": "٣"},
    {"type": "pair",
     "ar": "أي: الكلام على حذف المضاف بقرينة المقام.",
     "en": "That is, the expression is on the basis of an omitted muḍāf, indicated by the context."},

    # ---------------- Footnote 4 ----------------
    {"type": "note", "num": "٤"},
    {"type": "pair",
     "ar": "سورة البقرة:٧١.",
     "en": "Qurʾān, Sūrat al-Baqara 2:71."},

    # ---------------- Footnote 5 ----------------
    {"type": "note", "num": "٥"},
    {"type": "pair",
     "ar": "فإنه يدل على حصول الذبح، فلو كان المراد من قوله تعالى: ﴿وما كادوا يفعلون﴾ (البقرة:٧١) نفي القرب عن الذبح الذي يستلزم انتفاء الذبح على وجه أبلغ لزم التناقض.",
     "en": "For it indicates that the slaughter took place; so if what is meant by His words, the Exalted, “and they nearly did not do it” (Qurʾān, Sūrat al-Baqara 2:71) were the negation of nearness to the slaughter, which entails the absence of the slaughter in a more emphatic way, a contradiction would follow."},

    # ---------------- Footnote 6 ----------------
    {"type": "note", "num": "٦"},
    {"type": "pair",
     "ar": "سورة البقرة:٧١.",
     "en": "Qurʾān, Sūrat al-Baqara 2:71."},

    # ---------------- Footnote 7 ----------------
    {"type": "note", "num": "٧"},
    {"type": "pair",
     "ar": "سورة البقرة:٧١.",
     "en": "Qurʾān, Sūrat al-Baqara 2:71."},

    # ---------------- Footnote 8 ----------------
    {"type": "note", "num": "٨"},
    {"type": "pair",
     "ar": "سورة البقرة:٧١.",
     "en": "Qurʾān, Sūrat al-Baqara 2:71."},
]
