# -*- coding: utf-8 -*-
"""Mulla Jami — al-Fawāʾid al-Ḍiyāʾiyya. Source PDF page 455 (printed ٤٥٤)."""

PAGE_NUMBER = 455
PRINTED_PAGE = "٤٥٤"   # Arabic-Indic, as printed

BLOCKS = [
    # ---------------- The commentary text (matn) ----------------
    # Continues «… أي: حدث موضوعا» at the foot of PDF p. 454 (mid-sentence).
    {"type": "matn",
     "ar": "ذلك الاسم (لمن قام) أي: الفعل[[١]] (به) أي: لذات ما[[٢]] قام بها الفعل،",
     "en": "…that noun (for one in whom subsists), that is, the verb, (it), that is, for some essence in which the verb subsists."},
    {"type": "matn",
     "ar": "ولو قال: «لما قام به الفعل» لكان أولى؛ لأن ما جهل أمره[[٣]] يذكر بلفظة «ما»، ولعله قصد التغليب[[٤]]",
     "en": "Had he said “for that in which the verb subsists” it would have been better, because what is of unknown nature is referred to by the word “mā”; perhaps he intended predominance (taghlīb) [of the rational]."},
    {"type": "matn",
     "ar": "(بمعنى الحدوث) نعني بالحدوث: تجدد وجوده له، وقيامه به مقيدا بأحد الأزمنة الثلاثة.",
     "en": "(In the sense of occurrence (ḥudūth)): by occurrence we mean its existence coming anew to it, and its subsisting in it as restricted to one of the three times."},
    {"type": "matn",
     "ar": "قال المصنف في شرحه: قوله: «ما اشتق من فعل» يدخل فيه المحدود وغيره من اسم المفعول، والصفة المشبهة، وغير ذلك[[٥]]،",
     "en": "The author said in his commentary: his words “what is derived from a verb” include the thing defined and others, such as the passive participle, the resembling adjective and so on;"},
    {"type": "matn",
     "ar": "وقوله: «لمن قام به» يخرج منه ما عدا الصفة المشبهة؛ لأن الجميع ليس لمن قام به،",
     "en": "his words “for one in whom it subsists” exclude from it all but the resembling adjective, because none of them is for one in whom it subsists;"},
    {"type": "matn",
     "ar": "وقوله: «بمعنى الحدوث» يخرج الصفة المشبهة؛ لأن وضعها على أن تدل على معنى ثابت.",
     "en": "and his words “in the sense of occurrence” exclude the resembling adjective, because it is coined to denote a stable notion."},
    {"type": "matn",
     "ar": "والظاهر أن اسم التفضيل داخل في الجميع الذي حكم عليه بأنه ليس لمن قام به، والحق ذلك؛",
     "en": "What is apparent is that the noun of preference (ism al-tafḍīl) is included in the “all” of which he judged that it is not for one in whom [the verb] subsists; and that is the truth;"},
    {"type": "matn",
     "ar": "لأن المتبادر من قوله: «ما اشتق لمن قام به» أن يكون موضوعا لمن قام به، ويكون «من قام به» تمام المعنى الموضوع له من غير زيادة ونقصان،",
     "en": "for what is immediately understood from his words “what is derived for one in whom it subsists” is that it be coined for one in whom it subsists, and that “one in whom it subsists” be the whole of the meaning for which it is coined, without addition or deficiency."},
    # REVIEW: printed «كالزيادة فيهن» (feminine plural pronoun); the expected form is «فيه». Transcribed as printed, translated as «فيه».
    {"type": "matn",
     "ar": "فلو ضم إلى أصل الفعل معنى آخر كالزيادة فيهن ووضع له اسم لا يصدق على هذا الاسم أنه موضوع لمن قام به الفعل، بل لمن قام به الفعل مع زيادة،",
     "en": "So if another notion, such as an excess in it, were joined to the base of the verb and a noun were coined for that, it would not be true of this noun that it is coined for one in whom the verb subsists, but rather for one in whom the verb subsists with an excess."},
    {"type": "matn",
     "ar": "فبقوله: «لمن قام به» خرج اسم التفضيل[[٦]]، فإنه موضوع لمن قام به الفعل مع الزيادة على أصل الفعل.",
     "en": "Thus by his words “for one in whom it subsists” the noun of preference is excluded, for it is coined for one in whom the verb subsists with an excess over the base of the verb."},
    {"type": "matn",
     "ar": "وخالف أكثر الشارحين المصنف وأسندوا إخراج اسم التفضيل[[٧]] إلى قوله: «بمعنى الحدوث» كما أسندوا إخراج الصفة المشبهة إليه",
     "en": "Most of the commentators disagreed with the author and attributed the exclusion of the noun of preference to his words “in the sense of occurrence”, just as they attributed the exclusion of the resembling adjective to them,"},
    {"type": "matn",
     "ar": "ظنا منهم أن الاشتقاق لمن قام به شامل لاسم التفضيل، ولم يتنبهوا أن الاشتقاق متضمن معنى الوضع كما",
     "en": "supposing that derivation “for one in whom it subsists” includes the noun of preference; they did not notice that derivation includes the sense of coining, as…"},

    {"type": "rule"},

    # ---------------- Footnote 1 ----------------
    {"type": "note", "num": "١"},
    # REVIEW: printed «بناء على أن الضمير «يرد» إلى أقرب المذكورات» with «يرد» in guillemets; the guillemets look misplaced (the sense is "the pronoun is referred to the nearest of the things mentioned"). Transcribed as printed.
    {"type": "pair",
     "ar": "بيان لمرجع الضمير لدفع توهم رجوعه إلى «من» بناء على أن الضمير «يرد» إلى أقرب المذكورات.",
     "en": "This states what the pronoun refers to, to forestall the supposition that it refers to “man”, on the basis that a pronoun is referred to the nearest of the things mentioned."},

    # ---------------- Footnote 2 ----------------
    {"type": "note", "num": "٢"},
    {"type": "pair",
     "ar": "يعني: أن «من» موصوفة، وأن يعتبر في اسم الفاعل كون الذات المبهمة منسوبا إليه لا كون الفعل منسوبا كما يوهمه تقديم الفعل على «من»، فإنه لضرورة الاشتقاق.",
     "en": "He means that “man” is qualified [an indefinite noun], and that what is considered in the active participle is the indeterminate essence’s being that to which [the verb] is ascribed, not the verb’s being ascribed, as the placing of “the verb” before “man” suggests; for that is owing to the requirement of derivation."},

    # ---------------- Footnote 3 ----------------
    {"type": "note", "num": "٣"},
    {"type": "pair",
     "ar": "فيه أن أمره هو كونه شاملا لمن يعلم ومن لا يعلم؛ لأن النكرة الموصوفة تعم.",
     "en": "Against this: its nature is that it includes both what has knowledge and what does not, since a qualified indefinite noun is general."},

    # ---------------- Footnote 4 ----------------
    {"type": "note", "num": "٤"},
    {"type": "pair",
     "ar": "لكن مقام التعريف آب عنه.",
     "en": "But the setting of a definition rejects it."},

    # ---------------- Footnote 5 ----------------
    {"type": "note", "num": "٥"},
    {"type": "pair",
     "ar": "من الأسماء المشتقة.",
     "en": "Among the derived nouns."},

    # ---------------- Footnote 6 ----------------
    {"type": "note", "num": "٦"},
    # REVIEW: printed «كارمني فكرمته لكرمه»; the function of «لكرمه» here is unclear (the active participle would be «كارمه»/«كارم»). Transcribed as printed; English renders it literally.
    {"type": "pair",
     "ar": "ولا يخرج عنه اسم الفاعل من باب المغالبة، نحو: كارمني فكرمته لكرمه؛",
     "en": "The active participle of the pattern of contest (mughālaba) is not excluded by it, as in “kāramanī fa-karamtuhu” (he vied with me in generosity and I outdid him), “li-karamihi” (for his generosity);"},
    {"type": "pair",
     "ar": "لأنه موضوع للغلبة في معنى المصدر لا لمعنى المصدر مع الغلبة.",
     "en": "for it is coined for prevailing in the meaning of the verbal noun, not for the meaning of the verbal noun together with prevailing."},
    {"type": "pair",
     "ar": "في رضي الشافية: ونعني بباب المغالبة أن يغلب أحد الأمرين الآخر في معنى المصدر، نحو: كارمني فكرمته أي: غلبته في الكرم.",
     "en": "In al-Raḍī’s commentary on al-Shāfiya: by the pattern of contest we mean that one of two parties prevails over the other in the meaning of the verbal noun, as in “kāramanī fa-karamtuhu”, that is, I prevailed over him in generosity."},

    # ---------------- Footnote 7 ----------------
    {"type": "note", "num": "٧"},
    {"type": "pair",
     "ar": "بناء على أنه لا يدل على الحدث مقيدا بأحد الأزمنة الثلاثة، وإن كان قد يدل على الحدوث بمعنى التجدد.",
     "en": "On the basis that it does not denote the event as restricted to one of the three times, even if it sometimes denotes occurrence in the sense of coming anew."},
]
