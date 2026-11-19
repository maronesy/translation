# -*- coding: utf-8 -*-
"""Mulla Jami — al-Fawāʾid al-Ḍiyāʾiyya. Source PDF page 199 (printed ١٩٨)."""

PAGE_NUMBER = 199
PRINTED_PAGE = "١٩٨"   # Arabic-Indic, as printed

BLOCKS = [
    # ---------------- The commentary text (matn) ----------------
    # continues from page 198 ("…وقصد")
    {"type": "matn",
     "ar": "نداؤها، فهي في حكم من يطلب إقباله،",
     "en": "…calling them was intended; so they have the status of one whose turning is sought,"},
    # REVIEW: print reads «المنادي» (with yāʾ) twice in this paragraph where «المنادى» is expected; transcribed as printed.
    {"type": "matn",
     "ar": "بخلاف المندوب؛ لأنه المتفجع عليه، أدخل عليه حرف النداء لمجرد التفجع، لا لتنزيله منزلة المنادى، وقصد نداؤه، فخرج بهذا القيد عن تعريف المنادي.",
     "en": "unlike the lamented noun (al-mandūb); for it is the one over whom grief is expressed: the vocative particle is applied to it merely to express grief, not to treat it as a vocative with its calling intended. So by this condition it is excluded from the definition of the vocative."},
    {"type": "matn",
     "ar": "ولهذا أفرد المصنف أحكامه بالذكر فيما بعد، وفيه تحكم[[١]]،",
     "en": "For this reason the author treats its rules separately later on; but this is arbitrary (taḥakkum),"},
    {"type": "matn",
     "ar": "فإن المنادي المندوب أيضا كما قال بعضهم[[٢]]: منادى مطلوب إقباله حكما على وجه التفجع،",
     "en": "for the lamented vocative too, as one of them said, is a vocative whose turning is sought by status, by way of expressing grief:"},
    {"type": "matn",
     "ar": "فإذا قلت: «يا محمداه»، فكأنك تناديه وتقول له: «تعال فأنا مشتاق إليك».",
     "en": "when you say “yā Muḥammadāh!” it is as though you call him and say to him: “Come, for I long for you.”"},
    {"type": "matn",
     "ar": "فالأولى إدخاله تحت المنادى كما فعله صاحب المفصل[[٣]].",
     "en": "It is therefore better to include it under the vocative, as the author of al-Mufaṣṣal did."},
    {"type": "matn",
     "ar": "وقيل: الظاهر من كلام سيبويه أيضا أنه داخل في المنادى.",
     "en": "It has been said: what is apparent from Sībawayh’s words too is that it falls under the vocative."},
    {"type": "matn",
     "ar": "(بحرف نائب مناب «أدعو»[[٤]]) من الحروف الخمسة، وهي: «يا، وأيا، وهيا، وأي، والهمزة»[[٥]].",
     "en": "(By means of a particle standing in place of “adʿū” [I call]), one of the five particles, namely: “yā,” “ayā,” “hayā,” “ay” and the hamza."},
    {"type": "matn",
     "ar": "واحترز به عن نحو: «ليقبل زيد»[[٦]]",
     "en": "By this he guarded against such as “li-yuqbil Zaydun” (let Zayd come forward)."},
    {"type": "matn",
     "ar": "(لفظا أو تقديرا) تفصيل للطلب، أي: طلبا لفظيا بأن يكون آلة الطلب لفظية[[٧]] نحو: «يا زيد»",
     "en": "(Expressly or by supposition) is a specification of the seeking, that is: a seeking that is expressed, in that the instrument of seeking is uttered, as in “yā Zaydu,”"},
    {"type": "matn",
     "ar": "أو تقديريا بأن يكون آلته مقدرة نحو: ﴿يوسف أعرض عن هذا﴾[[٨]]،",
     "en": "or one that is supposed, in that its instrument is understood, as in: “Joseph, turn away from this”;"},
    {"type": "matn",
     "ar": "أو للنيابة أي: نيابة لفظية بأن يكون النائب",
     "en": "or [it specifies] the standing-in, that is: an expressed standing-in, in that what stands in…"},

    {"type": "rule"},

    # ---------------- Footnote 1 ----------------
    {"type": "note", "num": "١"},
    {"type": "pair",
     "ar": "يمكن دفعه بأن المندوب باب واسع كثير الدوران على ألسنتهم، فاستبعد جعله مجازا غير ملحق بالحقيقة، بخلاف ما عداه، فإنه قليل الوقوع.",
     "en": "This can be answered by [saying] that the lamented noun is a wide chapter, frequently on their tongues; so it was thought unlikely that it should be made a figurative use not assimilated to the literal, unlike the others, which occur rarely."},

    # ---------------- Footnote 2 ----------------
    {"type": "note", "num": "٢"},
    {"type": "pair",
     "ar": "هو الجزولي. ويؤيده قولهم في المراثي: لا تبعد أي: لا تهلك،",
     "en": "He is al-Jazūlī. It is supported by their saying in elegies: “lā tabʿad” (do not go far), that is: do not perish;"},
    {"type": "pair",
     "ar": "كأنهم من ضنهم بالميت تصوروه حيا، فكرهوا موته، فقالوا: لا تبعد أي: لا بعدت ولا هلكت.",
     "en": "as though, from their attachment to the dead man, they imagined him alive and were loath that he should die, so they said: “Do not go far,” that is: may you not have gone far nor perished."},

    # ---------------- Footnote 3 ----------------
    {"type": "note", "num": "٣"},
    {"type": "pair",
     "ar": "وكأنه منع المصنف عن ذلك أنهم لم يعدوا كلمة «وا» من حروف النداء.",
     "en": "It seems that what kept the author from this is that they did not count the word “wā” among the vocative particles."},

    # ---------------- Footnote 4 ----------------
    {"type": "note", "num": "٤"},
    {"type": "pair",
     "ar": "الإنشائي؛ لأن الجملة الندائية إنشائية. فالأولى: تقدير دعوت أو ناديت؛ لأن الأغلب في الأفعال الإنشائية مجيئها بلفظ الماضي.",
     "en": "[Adʿū] in the performative sense (inshāʾī), because the vocative sentence is performative. Better, then, is to suppose “daʿawtu” or “nādaytu,” because performative verbs mostly come in the form of the past."},

    # ---------------- Footnote 5 ----------------
    {"type": "note", "num": "٥"},
    {"type": "pair",
     "ar": "الأول أعم، والثاني للبعيد، والثلاثة الأخيرة للقريب،",
     "en": "The first is the most general, the second is for the distant, and the last three for the near."},
    {"type": "pair",
     "ar": "وهذه الخمسة سبعة في الحقيقة؛ لأن في الهمزة وأي لغتين، أعني القصر والمد، وبلفظ «وا» تصير أدوات النداء ثمانية.",
     "en": "These five are in reality seven, because the hamza and “ay” each have two forms, namely the short and the long; and with the word “wā” the vocative particles become eight."},
    {"type": "pair",
     "ar": "وإنما لم يذكره ههنا لما سبق أن المندوب عند المصنف غير معدود من المنادى.",
     "en": "He did not mention it here only because, as preceded, the lamented noun is not counted by the author among vocatives."},
    {"type": "pair",
     "ar": "واعلم أن «يا» أصل حروف النداء وأكثرها استعمالا، ولا يقدر عند الحذف سواها، ولا ينادى اسم الله إلا بها.",
     "en": "Know that “yā” is the basic vocative particle and the most used; no other is supposed when [the particle] is elided, and the name of Allah is called only with it."},

    # ---------------- Footnote 6 ----------------
    {"type": "note", "num": "٦"},
    {"type": "pair",
     "ar": "ولم يقل: «عن نحو: أطلب إقبال زيد» كما قال بعضهم؛ لأنه ظاهر في الإخبار، فلا يكون زيد مطلوبا إقباله، بل مخبرا عن طلب إقباله.",
     "en": "He did not say “against such as ‘I seek Zayd’s coming forward,’” as one of them said, because that is plainly a statement of information; so Zayd is not one whose coming forward is sought, but one about the seeking of whose coming forward information is given."},

    # ---------------- Footnote 7 ----------------
    {"type": "note", "num": "٧"},
    {"type": "pair",
     "ar": "الطلب اللفظي يتوقف على لفظية آلته والمطلوب، فأيهما قدر صار الطلب تقديريا، فالاحتمال الثالث من أقسام هذا الاحتمال، فتأمل.",
     "en": "Expressed seeking depends on both its instrument and what is sought being uttered; whichever of the two is supposed, the seeking becomes supposed. So the third possibility is one of the divisions of this possibility; so reflect."},

    # ---------------- Footnote 8 ----------------
    {"type": "note", "num": "٨"},
    {"type": "pair",
     "ar": "سورة يوسف: ٢٩.",
     "en": "Qurʾān, Sūrat Yūsuf 12:29."},
]
