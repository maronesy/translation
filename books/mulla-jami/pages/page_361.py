# -*- coding: utf-8 -*-
"""Mulla Jami — al-Fawāʾid al-Ḍiyāʾiyya. Source PDF page 361 (printed ٣٦٠)."""

PAGE_NUMBER = 361
PRINTED_PAGE = "٣٦٠"   # Arabic-Indic, as printed

BLOCKS = [
    # ---------------- The commentary text (matn) ----------------
    # Follows «… إنكن إنه (إلى «إنهن»).» at the foot of PDF p. 360 (new sentence).
    {"type": "matn",
     "ar": "(و) النوع (الرابع) أي: المنصوب المنفصل («إياي» إيانا، إياك، إياكما، إياكم، إياك، إياكما، إياكن إياه (إلى «إياهن»)).",
     "en": "(And the fourth) type, that is, the detached accusative, is (“iyyāya”, iyyānā, iyyāka, iyyākumā, iyyākum, iyyāki, iyyākumā, iyyākunna, iyyāhu, (to “iyyāhunna”))."},
    {"type": "matn",
     "ar": "وفي «إيا» اختلافات كثيرة، والمختار أن الضمير هو «إيا»، واللواحق للدلالة على التكلم والخطاب والغيبة والإفراد والتثنية والجمع والتذكير والتأنيث.",
     "en": "There are many disagreements over “iyyā”; the preferred view is that the pronoun is “iyyā”, and the suffixes serve to indicate first, second and third person, singular, dual and plural, masculine and feminine."},
    {"type": "matn",
     "ar": "(و) النوع (الخامس: «غلامي») مثال المتصل بالاسم (و«لي») مثال المتصل بالحرف،",
     "en": "(And the fifth) type is [the attached genitive]: (“ghulāmī” (my servant)), an example of the one attached to a noun, (and “lī” (to me)), an example of the one attached to a particle:"},
    {"type": "matn",
     "ar": "«غلامي، غلامنا، غلامك» (إلى «غلامهن») و«لي، لنا، لك» إلى («لهن»).",
     "en": "“ghulāmī, ghulāmunā, ghulāmuka” (to “ghulāmuhunna”), and “lī, lanā, laka” to (“lahunna”)."},
    {"type": "matn",
     "ar": "وكان القياس أن يكون ضمائر كل من المتكلم والمخاطب والغائب ستة،",
     "en": "Analogy would have required the pronouns of each of the first, second and third person to be six;"},
    {"type": "matn",
     "ar": "لكنهم وضعوا للمتكلم لفظين[[١]] يدلان على ستة معان[[٢]] كـ«ضربت وضربنا»،",
     "en": "but they coined for the first person two words that indicate six meanings, as in “ḍarabtu” and “ḍarabnā”:"},
    {"type": "matn",
     "ar": "فضمير «ضربت» مشترك بين الواحد المذكر والمؤنث، وضمير «ضربنا» بين الأربعة: «المثنى المذكر، والمثنى المؤنث، والجمع المذكر، والمجموع المؤنث»،",
     "en": "the pronoun of “ḍarabtu” is shared between the masculine and feminine singular, and the pronoun of “ḍarabnā” among the four: the masculine dual, the feminine dual, the masculine plural and the feminine plural."},
    {"type": "matn",
     "ar": "ووضعوا للمخاطب خمسة ألفاظ، أربعة غير مشتركة، وواحد مشترك بين المثنى المذكر والمثنى المؤنث،",
     "en": "For the second person they coined five words: four not shared, and one shared between the masculine dual and the feminine dual."},
    {"type": "matn",
     "ar": "وأعطوا الغائب حكم المخاطب[[٣]] في ذلك، فإن الضمير في مثل: «ضربا وضربتا» هو الألف المشترك بينهما، والتاء حرف تأنيث،",
     "en": "They gave the third person the status of the second person in this, for the pronoun in such as “ḍarabā” and “ḍarabatā” is the alif shared between them, and the tāʾ is a particle of the feminine."},
    {"type": "matn",
     "ar": "وبقية الأنواع الخمسة جارية على هذا المجرى أعني: أن للمتكلم لفظين، وللمخاطب خمسة، وللغائب خمسة، فصار المجموع اثنتي عشرة كلمة لثمانية عشر معنى،",
     "en": "The rest of the five types follow the same course, I mean: the first person has two words, the second person five and the third person five, so the total is twelve words for eighteen meanings."},
    {"type": "matn",
     "ar": "فإذا كان لكل من الأنواع الخمسة اثنتي عشرة كلمة لثمانية عشر معنى يكون جملتها ستين كلمة لتسعين معنى،",
     "en": "Since each of the five types has twelve words for eighteen meanings, their sum is sixty words for ninety meanings."},
    {"type": "matn",
     "ar": "وبينوا لتلك الأمور عللا ومناسبات لا نطول الكلام بذكرها.",
     "en": "They set out causes and correspondences for these matters, which we shall not lengthen the discussion by mentioning."},
    {"type": "matn",
     "ar": "(فالمرفوع المتصل خاصة[[٤]]) يعني: لا المنصوب والمجرور المتصلان (يستتر)؛",
     "en": "(The attached nominative specifically), that is, not the attached accusative and genitive, (is concealed),…"},

    {"type": "rule"},

    # ---------------- Footnote 1 ----------------
    {"type": "note", "num": "١"},
    {"type": "pair",
     "ar": "يدلان على ستة معان؛ لأن المشاهدة شاهدة على الفرق.",
     "en": "They indicate six meanings, because direct observation attests the difference."},

    # ---------------- Footnote 2 ----------------
    {"type": "note", "num": "٢"},
    {"type": "pair",
     "ar": "ظاهره أنه مشترك لفظي. والحق أنه مشترك معنوي، فإنه موضوع للمتكلم مع الغير أيا ما كان ذلك الغير،",
     "en": "Its apparent sense is that it is a homonym (mushtarak lafẓī). The truth is that it is a univocal common term (mushtarak maʿnawī), for it is coined for the speaker together with another, whoever that other may be."},
    {"type": "pair",
     "ar": "وأيضا دلالته على أكثر من ستة معان؛ لأنه يدل على المثنى المخلوط والجمع المخلوط أيضا بخلاف ضمير المثنى.",
     "en": "Also, it indicates more than six meanings, because it also indicates the mixed dual and the mixed plural, unlike the pronoun of the dual."},

    # ---------------- Footnote 3 ----------------
    {"type": "note", "num": "٣"},
    {"type": "pair",
     "ar": "وذلك مبني على تغاير الواحد الغائب والواحدة الغائبة قياسا على المرفوع المنفصل كهو وهي.",
     "en": "That rests on the third person masculine singular and feminine singular being distinct, by analogy with the detached nominative, such as “huwa” and “hiya”."},

    # ---------------- Footnote 4 ----------------
    {"type": "note", "num": "٤"},
    {"type": "pair",
     "ar": "في القاموس: الخاصة ضد العامة، وهو حال من فاعل «يستتر» أو من المبتدأ، والتاء للتأنيث أي: طائفة خاصة.",
     "en": "In al-Qāmūs: al-khāṣṣa is the opposite of al-ʿāmma. It is a circumstantial qualifier (ḥāl) of the agent of “yastatiru” or of the subject, and the tāʾ is feminine, that is, “a specific group”."},
    {"type": "pair",
     "ar": "وفي الهندي: التاء للمبالغة، أو الخاصة مصدر كالعافية والتقدير خص خصوصا، والجملة معترضة هذا،",
     "en": "In al-Hindī: the tāʾ is for intensification, or khāṣṣa is a verbal noun like ʿāfiya, the implied sense being “khaṣṣa khuṣūṣan”, the clause being parenthetical. So much for that."},
    {"type": "pair",
     "ar": "ولك أن تجعل الجملة حالا بتقدير قد خص خصوصا.",
     "en": "You may also make the clause a circumstantial qualifier by supposing “qad khaṣṣa khuṣūṣan”."},
    {"type": "pair",
     "ar": "قال عبد الغفور: قيل: حال من ضمير «يستتر»، والتاء للمبالغة لا للتأنيث، أو مصدر كالكاذبة منصوب بمحذوف أي: أخص بالاستتار خصوصا، والجملة معترضة.",
     "en": "ʿAbd al-Ghafūr said: it has been said that it is a circumstantial qualifier of the pronoun of “yastatiru”, the tāʾ being for intensification, not the feminine; or a verbal noun like kādhiba, in the accusative by an elided [verb], that is, “I single out concealment specifically”, the clause being parenthetical."},
]
