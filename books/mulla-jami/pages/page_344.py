# -*- coding: utf-8 -*-
"""Mulla Jami — al-Fawāʾid al-Ḍiyāʾiyya. Source PDF page 344 (printed ٣٤٣)."""

PAGE_NUMBER = 344
PRINTED_PAGE = "٣٤٣"   # Arabic-Indic, as printed

BLOCKS = [
    # ---------------- The commentary text (matn) ----------------
    # Continues «… وذلك الدفع يكون» from the foot of PDF p. 343.
    {"type": "matn",
     "ar": "بتكرير اللفظ نحو: «ضرب زيد زيد» أو «ضرب ضرب زيد»",
     "en": "… by repeating the word, as in “ḍaraba Zaydun Zaydun” (Zayd, Zayd struck) or “ḍaraba ḍaraba Zaydun” (Zayd struck, struck);"},
    {"type": "matn",
     "ar": "أو لدفع ظن السامع به تجوزا: إما في المنسوب نحو قولك: «زيد قتيل قتيل» دفعا لتوهم السامع أن يريد بالقتل الضرب الشديد، فيجب حينئذ أيضا تكرير اللفظ حتى لا يبقى شك في إرادة المعنى الحقيقي،",
     "en": "or to ward off the hearer’s supposing that he is speaking figuratively (tajawwuz): either in the thing attributed, as in your saying “Zaydun qatīlun qatīlun” (Zayd is slain, slain), to ward off the hearer’s imagining that by “slaying” he means a severe beating; here too repetition of the word is then required, so that no doubt remains that the literal meaning is intended;"},
    {"type": "matn",
     "ar": "أو في المنسوب إليه، فإنه ربما نسب الفعل إلى شيء، والمراد نسبته إلى بعض متعلقاته، كما في «قطع الأمير اللص» أي: قطع غلامه،",
     "en": "or in that to which it is attributed, for an act is sometimes attributed to a thing when what is meant is its attribution to something connected with it, as in “qaṭaʿa al-amīru al-liṣṣa” (the emir cut [the hand of] the thief), that is, his servant cut it."},
    {"type": "matn",
     "ar": "فيجب حينئذ تكرير المنسوب إليه لفظا نحو: «ضرب زيد زيد» أي: ضرب هو لا من يقوم مقامه، أو تكريره معنى نحو: «ضرب زيد نفسه أو عينه»",
     "en": "Repetition of that to which it is attributed is then required, either in wording, as in “ḍaraba Zaydun Zaydun”, that is, he himself struck, not someone standing in his place; or in meaning, as in “ḍaraba Zaydun nafsuhu aw ʿaynuhu” (Zayd himself struck)."},
    {"type": "matn",
     "ar": "(أو في الشمول) أي: التأكيد ما يقرر أمر المتبوع[[١]] في النسبة بالتفصيل الذي ذكرناه، أو في شمول المتبوع أفراده دفعا لظن السامع تجوزا لا في نفس المنسوب إليه بل في شموله لإفراده",
     # REVIEW: «لإفراده» (with hamza under the alif) printed here; the repeated clause below has «لأفراده». Transcribed as printed.
     "en": "(Or in comprehensiveness [shumūl]), that is, the corroborative is what establishes the matter of the word followed in the attribution, in the detail we have set out, or in the word followed comprehending its individual members, to ward off the hearer’s supposing a figurative usage, not in that to which it is attributed itself but in its comprehending its members,"},
    {"type": "matn",
     # REVIEW: the clause «فإنه كثيرا ما ينسب الفعل إلى جميع أفراد المنسوب إليه، بل في شموله لأفراده» is printed twice in succession (apparent dittography); transcribed as printed.
     "ar": "فإنه كثيرا ما ينسب الفعل إلى جميع أفراد المنسوب إليه، بل في شموله لأفراده، فإنه كثيرا ما ينسب الفعل إلى جميع أفراد المنسوب إليه مع أنه يريد النسبة إلى بعضها،",
     "en": "for an act is often attributed to all the members of that to which it is attributed, but in its comprehending its members, for an act is often attributed to all the members of that to which it is attributed while he intends the attribution to some of them."},
    {"type": "matn",
     "ar": "فيندفع هذا الوهم بذكر «كل وأجمع» وأخواته، و«كلاهما وثلاثتهم وأربعتهم» ونحوها، فهذا هو الغرض[[٢]] من جميع ألفاظ التأكيد.",
     "en": "This misconception is warded off by mentioning “kull” and “ajmaʿ” and their sisters, and “kilāhumā”, “thalāthatuhum”, “arbaʿatuhum” and the like. This, then, is the purpose of all the words of corroboration."},
    {"type": "matn",
     "ar": "وإذا عرفت هذا فنقول: أخرج المصنف الصفة والعطف والبدل عن حد التأكيد بقوله: «يقرر أمر المتبوع».",
     "en": "Once you know this, we say: the author excluded the qualifier (ṣifa), the conjunction (ʿaṭf) and the substitute (badal) from the definition of the corroborative by his words “that establishes the matter of the word it follows”."},
    {"type": "matn",
     "ar": "أما البدل والعطف: فظاهر خروجهما به[[٣]].",
     "en": "As for the substitute and the conjunction, their exclusion by it is evident."},
    {"type": "matn",
     "ar": "وأما الصفة: فلأن وضعها للدلالة على معنى في متبوعها، وأفادتها توضيح متبوعها في بعض المواضع ليست بالوضع.",
     # REVIEW: «وأفادتها» printed (alif with hamza above); footnote ٢ quotes it as «وإفادتها». Transcribed as printed.
     "en": "As for the qualifier, it is because it is coined to indicate a meaning in the word it follows, and its conveying the clarification of the word it follows in some places is not by coinage (waḍʿ)."},
    {"type": "matn",
     "ar": "وأما عطف البيان: فهو لتوضيح متبوعه، فهو يقرر أمر متبوعه ويحققه لكن لا في النسبة والشمول، هذا حاصل ما ذكره المصنف في شرحه.",
     "en": "As for the explicative apposition (ʿaṭf al-bayān), it serves to clarify the word it follows; it therefore establishes and verifies the matter of the word it follows, but not in the attribution or in comprehensiveness. This is the gist of what the author stated in his commentary."},

    {"type": "rule"},

    # ---------------- Footnote 1 ----------------
    {"type": "note", "num": "١"},
    {"type": "pair",
     # REVIEW: «إن جاء القوم» printed; the sense calls for «أن». Transcribed as printed.
     "ar": "نبه بذلك على أن ذكر \"أو\" في الشمول بعد قوله: في النسبة ليس لغوا لظهور إن جاء القوم كلهم أيضا يقرر أمر المتبوع في النسبة، ويفيد أن النسبة إلى الجميع لا إلى بعضه،",
     "en": "By this he draws attention to the fact that mentioning “or in comprehensiveness” after his words “in the attribution” is not redundant, since it is evident that “jāʾa al-qawmu kulluhum” (the people came, all of them) also establishes the matter of the word followed in the attribution, and conveys that the attribution is to the whole, not to part of it."},
    {"type": "pair",
     "ar": "ومفاد التنبيه أن يقرر أمر المتبوع في النسبة شاع فيما بينهم في التفصيل المذكور وليس له الشمول حتى يغني عن ذكر الشمول.",
     "en": "The point of the remark is that “establishes the matter of the word followed in the attribution” is current among them in the detail mentioned, and does not cover comprehensiveness, so as to make mentioning comprehensiveness unnecessary."},

    # ---------------- Footnote 2 ----------------
    {"type": "note", "num": "٢"},
    {"type": "pair",
     "ar": "أي: تقرير أمر المتبوع في النسبة أو الشمول هو الغرض من جميع ألفاظ التأكيد، فالتعريف به جامع لجميع الأفراد.",
     "en": "That is, establishing the matter of the word followed in the attribution or in comprehensiveness is the purpose of all the words of corroboration, so the definition by it includes all the members [of the defined]."},
    {"type": "pair",
     "ar": "وإذا عرفت هذا أي: كونه جامعا لجميع الأفراد فتقول: أخرج المصنف الصفة والعطف إلى آخره، فظهر أن التعريف جامع ومانع.",
     "en": "“Once you know this”, that is, its including all the members, “you say: the author excluded the qualifier and the conjunction …” to the end; so it becomes evident that the definition is inclusive and exclusive (jāmiʿ wa-māniʿ)."},
    {"type": "pair",
     "ar": "وقوله: وإفادتها توضيح متبوعها في بعض المواضع ليست بالوضع لو تعرض لتأكيد متبوعها لكان أنسب.",
     "en": "As for his words “and its conveying the clarification of the word it follows in some places is not by coinage”, had he addressed its corroborating the word it follows, it would have been more fitting."},

    # ---------------- Footnote 3 ----------------
    {"type": "note", "num": "٣"},
    {"type": "pair",
     "ar": "لكن في إخراج بدل الكل احتيج إلى منبه، وهو أن المبدل منه في حكم التنحية، فلا يمكن أن يكون تقريره مقصودا لتنافيهما.",
     "en": "But in excluding the whole-for-whole substitute (badal al-kull) a pointer was needed, namely that the word substituted for is treated as set aside, so its establishment cannot be intended, the two being incompatible."},
]
