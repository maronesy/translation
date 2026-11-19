# -*- coding: utf-8 -*-
"""Mulla Jami — al-Fawāʾid al-Ḍiyāʾiyya. Source PDF page 593 (printed ٥٩٢)."""

PAGE_NUMBER = 593
PRINTED_PAGE = "٥٩٢"   # Arabic-Indic, as printed

BLOCKS = [
    # ---------------- The commentary text (matn) ----------------
    # Continues «فسمي ما به ينون الشيء –» at the foot of PDF p. 592 (mid-sentence).
    # REVIEW: printed «وعرضوه» as transcribed; the sense requires «وعروضه» (its being accidental), translated so.
    {"type": "matn",
     "ar": "أعني: النون – تنوينا، إشعارا بحدوثه وعرضوه لما في المصدر من معنى الحدوث.",
     "en": "…I mean the nūn — tanwīn, to signal its being occasioned and accidental, because of the sense of occurrence (ḥudūth) that lies in the verbal noun (maṣdar)."},
    {"type": "matn",
     "ar": "ولهذا سمى سيبويه المصدر حدثا.",
     "en": "For this reason Sībawayh called the verbal noun “ḥadath” (event)."},
    {"type": "matn",
     "ar": "وهو في الاصطلاح: (نون ساكنة) أي: بذاتها، فلا تضرها الحركة العارضة، مثل ﴿عادا الأولى﴾[[١]].",
     "en": "In technical usage it is (a quiescent nūn), that is, quiescent in itself, so an accidental vowel does not impair it, as in “ʿĀdan al-ūlā” (ʿĀd of old)."},
    {"type": "matn",
     "ar": "وهي شاملة نون «من، ولدن، ولم يكن» وأمثالها.",
     "en": "This includes the nūn of “min”, “ladun”, “lam yakun” and the like."},
    {"type": "matn",
     "ar": "فأخرجها بقوله: (تتبع حركة الآخر) أي: آخر الكلمة، فإن هذه النونات أواخر تلك الكلمات لا توابع حركات أواخرها.",
     "en": "So he excluded them by his words (which follows the vowel of the end), that is, the end of the word; for these nūns are the ends of those words, not followers of the vowels of their ends."},
    {"type": "matn",
     "ar": "وإنما قال: «تتبع حركة الآخر» ولم يقل: «تتبع الآخر»؛ لأن المتبادر من متابعتها الآخر لحوقها به من غير تخلل شيء، وههنا الحركة متخللة بين آخر الكلمة والتنوين.",
     "en": "He said “follows the vowel of the end” and did not say “follows the end” only because what first comes to mind from its following the end is its attaching to it with nothing intervening, whereas here the vowel intervenes between the end of the word and the tanwīn."},
    {"type": "matn",
     "ar": "فإن قلت: فآخر الكلمة هي الحركة، فلا حاجة إلى ذكر الحركة؟",
     "en": "If you say: the end of the word is the vowel, so there is no need to mention the vowel?"},
    {"type": "matn",
     "ar": "قلت: المتبادر من الآخر الحرف الآخر.",
     "en": "I say: what first comes to mind from “the end” is the final letter."},
    {"type": "matn",
     "ar": "ولم يقل: «آخر الاسم»، ليشمل تنوين الترنم في الفعل (لا لتأكيد الفعل) فخرج نون التأكيد الخفيفة.",
     "en": "He did not say “the end of the noun”, so as to include the tanwīn of chanting (tarannum) in the verb. (Not for the corroboration of the verb): thus the light nūn of corroboration (nūn al-taʾkīd al-khafīfa) is excluded."},
    {"type": "matn",
     "ar": "ولا ينتقض التعريف بالنون في نحو: «يا رجل انطلق»، فإن المراد بتبعيتها حركة الآخر تطفلها لها في الوجود تطفل العارض للمعروض،",
     "en": "The definition is not broken by the nūn in, for example, “yā rajulu-nṭaliq” (O man, go), for what is meant by its following the vowel of the end is its depending on it for its existence, as the accident depends on its substrate;"},
    {"type": "matn",
     "ar": "وليس نون «انطلق» تابعا لحركة لام الرجل بهذا المعنى.",
     "en": "and the nūn of “inṭaliq” does not follow the vowel of the lām of “al-rajul” in this sense."},
    {"type": "matn",
     "ar": "(وهو) أي: التنوين (للتمكن) وهو: ما يدل على أمكنية الكلمة، أي: كون الاسم لم يشبه الفعل بالوجهين المعتبرين في منع الصرف، وحينئذ لا يتصور معناه في غير المنصرف.",
     "en": "(It), that is, the tanwīn, is (for full declinability (tamakkun)): this is what indicates that the word is fully declinable (amkaniyya), that is, that the noun does not resemble the verb in the two respects taken into account in diptosy (manʿ al-ṣarf); so its meaning is not conceivable in a diptote."},
    {"type": "matn",
     "ar": "(والتنكير) وهو الفارق بين المعرفة والنكرة، فهو الدال على أن مدخوله غير معين،",
     "en": "(And for indefiniteness (tankīr)): this is what distinguishes the definite from the indefinite; it indicates that what it enters upon is not specified,"},
    {"type": "matn",
     "ar": "نحو: «صه»، أي: «أسكت سكوتا ما في وقت ما»، وأما «صه» بغير التنوين، فمعناه: «أسكت السكوت الآن».",
     "en": "as in “ṣahin”, that is, “be silent, some silence, at some time”; whereas “ṣah” without tanwīn means “be silent, the silence [now required], now”."},
    {"type": "matn",
     "ar": "وأما التنوين في نحو: «أحمد وإبراهيم» فليس للتنكير، بل هو للتمكن.",
     "en": "As for the tanwīn in, for example, “Aḥmadun” and “Ibrāhīmun”, it is not for indefiniteness but for full declinability."},
    {"type": "matn",
     "ar": "قال الشارح الرضي: وأنا لا أرى منعا من أن يكون تنوين واحد للتمكن والتنكير",
     "en": "The commentator al-Raḍī said: “I see no obstacle to a single tanwīn being for full declinability and indefiniteness…"},

    {"type": "rule"},

    # ---------------- Footnote 1 ----------------
    {"type": "note", "num": "١"},
    {"type": "pair",
     "ar": "سورة النجم: ٥٠.",
     "en": "Qurʾān, Sūrat al-Najm 53:50."},
]
