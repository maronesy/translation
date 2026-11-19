# -*- coding: utf-8 -*-
"""Mulla Jami — al-Fawāʾid al-Ḍiyāʾiyya. Source PDF page 490 (printed ٤٨٩)."""

PAGE_NUMBER = 490
PRINTED_PAGE = "٤٨٩"   # Arabic-Indic, as printed

BLOCKS = [
    # ---------------- The commentary text (matn) ----------------
    # The page opens with a new item of the list begun on PDF p. 489 («(و«إذن»)…»).
    {"type": "matn",
     "ar": "(و«كي»، وبـ«أن» مقدرة بعد «حتى») نحو: «سرت حتى أدخلها».",
     "en": "(And “kay”; and by “an” supposed after “ḥattā”), as in “I travelled until I entered it”;"},
    {"type": "matn",
     "ar": "(و) بعد («لام» كي) نحو: «سرت لأدخلها».",
     "en": "(and) after (the “lām” of kay), as in “I travelled in order to enter it”;"},
    {"type": "matn",
     "ar": "(و) بعد («لام» الجحود) وهي اللام الجارة[[١]] الزائدة في خبر «كان» المنفي، نحو قوله تعالى: ﴿وما كان الله ليعذبهم﴾[[٢]]؛",
     "en": "(and) after (the “lām” of denial (juḥūd)), which is the governing-genitive, redundant lām in the predicate of negated “kāna”, as in His words, the Exalted: “But Allah would not punish them”;"},
    {"type": "matn",
     "ar": "لأن هذه الثلاثة جوار، فيمتنع دخولها على الفعل، إلا بجعلها مصدرا بتقدير «أن» المصدرية.",
     "en": "because these three govern the genitive, so their entering upon the verb is impossible except by making it a verbal noun through supposing the infinitival “an”."},
    {"type": "matn",
     "ar": "(و) بعد (الفاء) نحو: «زرني فأكرمك».",
     "en": "(And) after (the fāʾ), as in “Visit me, and I will honour you”;"},
    {"type": "matn",
     "ar": "(و) بعد (الواو) نحو: «لا تأكل السمك وتشرب اللبن»؛",
     "en": "(and) after (the wāw), as in “Do not eat fish and drink milk”;"},
    {"type": "matn",
     "ar": "فإن الفاء والواو عاطفتان واقعتان بعد الإنشاء، وقد امتنع عطف الخبر على الإنشاء، فجعل مفردا ليكون من قبيل عطف المفرد على المفرد المفهوم من ذلك الإنشاء،",
     "en": "for the fāʾ and the wāw are coordinating particles occurring after a performative utterance (inshāʾ), and coordinating an informative statement (khabar) with a performative is not permitted; so [the verb] was made a single term, so that it would be a case of coordinating a single term with the single term understood from that performative;"},
    {"type": "matn",
     "ar": "فيكون المعنى في «زرني فأكرمك»؛ ليكن زيارة منك فإكرام مني إياك، وفي «لا تأكل السمك وتشرب اللبن»؛ لا يكن منك أكل السمك وشرب اللبن معه.",
     "en": "so the meaning in “Visit me, and I will honour you” is “Let there be a visit from you and then an honouring of you from me”; and in “Do not eat fish and drink milk” it is “Let there not be from you the eating of fish together with the drinking of milk”."},
    {"type": "matn",
     "ar": "(و) بعد (أو) نحو: «لألزمنك أو تعطيني حقي».",
     "en": "(And) after (aw), as in “I will surely stick to you until you give me my due”."},
    {"type": "matn",
     "ar": "(فـ«أن») التي ينتصب بها المضارع (مثل: «أريد أن تحسن إلي») مثال النصب بالفتحة.",
     "en": "(So “an”), by which the muḍāriʿ is put in the accusative, (as in “I want you to do good to me”): an example of the accusative with the fatḥa,"},
    {"type": "matn",
     "ar": "(و) مثل: (﴿وأن تصوموا خير لكم﴾[[٣]])، مثال النصب بحذف النون.",
     "en": "(and as in “And that you fast is better for you”): an example of the accusative by omission of the nūn."},
    {"type": "matn",
     "ar": "(و) كلمة «أن» (التي تقع بعد العلم) إذا لم يكن بمعنى الظن[[٤]]، (هي) «أن»",
     "en": "(And) the word “an” (that occurs after [a verb of] knowledge), when it is not in the sense of supposition, (is) the “an”…"},

    {"type": "rule"},

    # ---------------- Continuation of footnote ٦ from PDF p. 489 ----------------
    # Unnumbered: runs on from footnote ٦ of printed p. ٤٨٨ (the quotation from al-Raḍī, «… فتقول: إذن»).
    {"type": "note", "num": ""},
    {"type": "pair",
     "ar": "أكرمك أي: إذ تزورني أكرمك أي: وقت زيارتك أكرمك،",
     "en": "…akrimaka’ (then I will honour you), that is, ‘when you visit me I will honour you’, that is, ‘at the time of your visit I will honour you’;"},
    {"type": "pair",
     "ar": "وعوض التنوين عن المضاف إليه؛ لأنه وضع في الأصل لازم الإضافة.",
     "en": "and the tanwīn was given in compensation for the term annexed to it, because it was originally coined as necessarily annexed.”"},

    # ---------------- Footnote 1 ----------------
    {"type": "note", "num": "١"},
    {"type": "pair",
     "ar": "عند البصريين فإنهم قالوا: إنه حرف جر متعلق بخبر «كان» المحذوف، والأصل ما كان قاصدا للفعل.",
     "en": "According to the Baṣrans, for they said: it is a genitive particle attached to the omitted predicate of “kāna”, the base being “he was not intending to do the act”."},
    # REVIEW: printed «الكفويين» for «الكوفيين»; transcribed as printed, translated as «الكوفيين».
    {"type": "pair",
     "ar": "وأما عند الكفويين، فحرف زائد لتأكيد النفي كالباء في «ما زيد بقائم» ناصب لم يتعلق بشيء، كذا في معنى اللبيب.",
     "en": "According to the Kūfans, however, it is a redundant particle for emphasizing the negation, like the bāʾ in “mā Zaydun bi-qāʾimin” (Zayd is not standing), governing the accusative and not attached to anything; so in Mughnī al-labīb."},
    # REVIEW: printed «معنى اللبيب» for the title «مغني اللبيب»; transcribed as printed.
    # REVIEW: printed «لقول بزيادته» where «القول بزيادته» would be expected; transcribed as printed.
    {"type": "pair",
     "ar": "فإن قلت: إذا كان للتعدية، فكيف يصح قوله: الزائدة؟ قلت: كثيرا ما يطلق لقول بزيادته لاطراد صحة إسقاطها، كذا في التحفة.",
     "en": "If you say: if it is for transitivity, how can his word “redundant” be valid? I say: it is often called redundant because its omission is regularly acceptable; so in al-Tuḥfa."},

    # ---------------- Footnote 2 ----------------
    {"type": "note", "num": "٢"},
    {"type": "pair",
     "ar": "سورة الأنفال: ٣٣.",
     "en": "Qurʾān, Sūrat al-Anfāl 8:33."},

    # ---------------- Footnote 3 ----------------
    {"type": "note", "num": "٣"},
    {"type": "pair",
     "ar": "سورة البقرة: ١٨٤.",
     "en": "Qurʾān, Sūrat al-Baqara 2:184."},

    # ---------------- Footnote 4 ----------------
    {"type": "note", "num": "٤"},
    {"type": "pair",
     "ar": "هذا يشعر بأن العلم جاء بمعنى الظن، والمشهور أنه لا يستعمل إلا في اليقين.",
     "en": "This suggests that knowledge (ʿilm) has occurred in the sense of supposition (ẓann), whereas the well-known view is that it is used only for certainty."},
    {"type": "pair",
     "ar": "ولو سلم فالمراد ليس لفظ العلم، حتى يصح تقييده بهذا، بل ما يدل على اليقين سواء كان لفظ العلم أو الرؤية أو الوجدان أو الظن أو غير ذلك.",
     "en": "Even if this is granted, what is meant is not the word ʿilm, so that restricting it by this would be valid, but whatever indicates certainty, whether it is the word ʿilm, ruʾya (seeing), wijdān (finding), ẓann, or something else."},
]
