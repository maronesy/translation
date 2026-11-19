# -*- coding: utf-8 -*-
"""Mulla Jami — al-Fawāʾid al-Ḍiyāʾiyya. Source PDF page 565 (printed ٥٦٤)."""

PAGE_NUMBER = 565
PRINTED_PAGE = "٥٦٤"   # Arabic-Indic, as printed

BLOCKS = [
    # ---------------- The commentary text (matn) ----------------
    {"type": "matn",
     "ar": "(وشذ إعمالها) أي: إعمال المفتوحة المخففة (في غيره) أي: في غير ضمير الشأن،",
     "en": "(And its governing is anomalous), that is, the governing of the lightened open [an], (in anything other than it), that is, other than the pronoun of the matter;"},
    {"type": "matn",
     "ar": "ولكنه قد حكى بعض أهل اللغة إعمالها في المضمر في السعة نحو قولهم: «أظن أنك قائم» و«أحسب أنه ذاهب».",
     "en": "but some of the lexicographers have reported its governing a pronoun in the ordinary range of speech, as in their saying “aẓunnu an-ka qāʾimun” (I think that you are standing) and “aḥsabu an-hu dhāhibun” (I reckon that he is going)."},
    {"type": "matn",
     "ar": "وهذه رواية شاذة غير معروفة.",
     "en": "This is an anomalous, unrecognized report."},
    {"type": "matn",
     "ar": "وأما في الضرورة، فجاء في المضمر فقط.",
     "en": "As for poetic necessity (ḍarūra), it has occurred only with a pronoun."},
    {"type": "matn",
     "ar": "قال الشاعر:",
     "en": "The poet said:"},
    {"type": "verse",
     "ar": "فلو أنك في يوم الرخاء سألتني          فراقك لم أبخل وأنت صديق",
     "en": "“Had you, on a day of ease, asked me for your parting, I would not have been niggardly, while you are a friend.”"},
    {"type": "matn",
     "ar": "(ويلزمها) أي: المفتوحة المخففة حال كونها مقرونة (مع الفعل) أي: الفعل المتصرف، بخلاف غير المتصرف، مثل ﴿وأن ليس للإنسان إلا ما سعى﴾[[١]]، ﴿وأن عسى أن يكون قد اقترب أجلهم﴾[[٢]].",
     "en": "(And there must accompany it), that is, the lightened open [an], when it is joined (with a verb), that is, a fully conjugable (mutaṣarrif) verb, unlike a non-conjugable one, as in “and that (wa-an) man has nothing but what he strives for” and “and that (wa-an) perhaps their term has drawn near”,"},
    {"type": "matn",
     "ar": "(السين) نحو: ﴿علم أن سيكون منكم مرضى﴾[[٣]].",
     "en": "(the sīn), as in: “He knows that (an) there will be among you some who are sick”;"},
    {"type": "matn",
     "ar": "(أو «سوف») كقول الشاعر:",
     "en": "(or “sawfa”), as in the poet’s words:"},
    {"type": "verse",
     "ar": "واعلم فعلم المرء ينفعه          أن سوف يأتي كل ما قدرا",
     "en": "“And know — for a man’s knowledge benefits him — that (an) all that has been decreed will come.”"},
    {"type": "matn",
     "ar": "(أو «قد») نحو: ﴿ليعلم أن قد أبلغوا رسالات ربهم﴾[[٤]].",
     "en": "(or “qad”), as in: “that He may know that (an) they have conveyed the messages of their Lord”."},
    {"type": "matn",
     "ar": "ولزوم هذه الأمور الثلاثة للفرق بين المخففة وبين «أن» المصدرية الناصبة، وليكون كالعوض من النون المحذوفة.",
     "en": "These three things are required in order to distinguish the lightened [an] from the infinitival “an” (al-maṣdariyya) that puts [the verb] in the subjunctive, and so that [the added element] be like a compensation for the elided nūn."},
    {"type": "matn",
     "ar": "(أو حرف النفي[[٥]]) نحو: ﴿أفلا يرون ألا يرجع إليهم قولا﴾[[٦]].",
     "en": "(Or a particle of negation), as in: “Do they not see that (allā) it does not return to them a word?”"},
    {"type": "matn",
     "ar": "وليس لزوم حرف النفي إلا ليكون كالعوض من النون المحذوفة.",
     "en": "The particle of negation is required only so that it be like a compensation for the elided nūn."},

    {"type": "rule"},

    # ---------------- Footnotes ----------------
    {"type": "note", "num": "١"},
    {"type": "pair",
     "ar": "سورة النجم: ٣٩.",
     "en": "Qurʾān, Sūrat al-Najm 53:39."},

    {"type": "note", "num": "٢"},
    {"type": "pair",
     "ar": "سورة الأعراف: ١٨٥.",
     "en": "Qurʾān, Sūrat al-Aʿrāf 7:185."},

    {"type": "note", "num": "٣"},
    {"type": "pair",
     "ar": "سورة المزمل: ٢٠.",
     "en": "Qurʾān, Sūrat al-Muzzammil 73:20."},

    {"type": "note", "num": "٤"},
    {"type": "pair",
     "ar": "سورة الجن: ٢٨.",
     "en": "Qurʾān, Sūrat al-Jinn 72:28."},

    {"type": "note", "num": "٥"},
    {"type": "pair",
     "ar": "نحو: علمت أن لم يقم، ولن يقوم، ولا يقوم، وما قام، وما يقوم.",
     "en": "As in: “I knew that he did not stand (an lam yaqum)”, “… will not stand (wa-lan yaqūma)”, “… does not stand (wa-lā yaqūmu)”, “… did not stand (wa-mā qāma)” and “… is not standing (wa-mā yaqūmu)”."},

    {"type": "note", "num": "٦"},
    {"type": "pair",
     "ar": "سورة طه: ٨٩.",
     "en": "Qurʾān, Sūrat Ṭāhā 20:89."},
]
