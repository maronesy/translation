# -*- coding: utf-8 -*-
"""Mulla Jami — al-Fawāʾid al-Ḍiyāʾiyya. Source PDF page 597 (printed ٥٩٦)."""

PAGE_NUMBER = 597
PRINTED_PAGE = "٥٩٦"   # Arabic-Indic, as printed

BLOCKS = [
    # ---------------- The commentary text (matn) ----------------
    # Continues «(وما قبلها) … (مع ضمير المذكرين)» at the foot of PDF p. 596.
    {"type": "matn",
     "ar": "وهو الواو (مضموم) ليدل على الواو المحذوفة لالتقاء الساكنين،",
     "en": "…which is the wāw, (takes a ḍamma), to point to the wāw elided because of the meeting of two quiescents,"},
    {"type": "matn",
     "ar": "وإن اشترط في التقاء الساكنين على حده أن يكون الساكنان في كلمة واحدة، فإن النون المشددة كلمة أخرى،",
     "en": "if, for the meeting of two quiescents in its proper form (ʿalā ḥaddihi), it is stipulated that the two quiescents be in a single word — for the doubled nūn is another word;"},
    {"type": "matn",
     "ar": "أو لثقل الواو بعد الضمة وقبل النون المشددة إن لم يشترط في التقاء الساكنين ما ذكر.",
     "en": "or because of the heaviness of the wāw after the ḍamma and before the doubled nūn, if what was mentioned is not stipulated for the meeting of two quiescents."},
    {"type": "matn",
     "ar": "(ومع) ضمير (المخاطبة) وهو الياء (مكسور) ليدل على الياء المحذوفة لالتقاء الساكنين، أو لثقل الياء بعد الكسرة وقبل النون المشددة.",
     "en": "(And with) the pronoun of (the feminine addressee), which is the yāʾ, (it takes a kasra), to point to the yāʾ elided because of the meeting of two quiescents, or because of the heaviness of the yāʾ after the kasra and before the doubled nūn."},
    {"type": "matn",
     "ar": "(و) ما قبلها (فيما عدا ذلك) المذكور من ضمير المذكرين وضمير المخاطبة، وهو الواحد المذكر -غائبا كان أو مخاطبا- والمؤنث الغائبة (مفتوح) طلبا للخفة.",
     "en": "(And) what precedes it (in what is other than that) mentioned — the pronoun of masculine plurals and the pronoun of the feminine addressee — namely the masculine singular, whether absent or addressed, and the absent feminine, (takes a fatḥa), seeking lightness."},
    {"type": "matn",
     "ar": "وظاهر أن ما عدا ذلك المذكور يشمل التثنية والجمع المؤنث، وحكمهما غير ما ذكر.",
     "en": "It is evident that “what is other than that mentioned” includes the dual and the feminine plural, and their rule is other than what was mentioned."},
    {"type": "matn",
     "ar": "فقوله: (وتقول في التثنية، وجمع المؤنث: «اضربان»، و«اضربنان») بمنزلة الاستثناء عنه.",
     "en": "So his words (and you say in the dual and the feminine plural: “iḍribānni” and “iḍribnānni”) stand as an exception to it."},
    {"type": "matn",
     "ar": "فتقول في المثنى: «اضربان» بإثبات الألف، لئلا يشتبه بالواحد و«اضربنان» في الجمع المؤنث بزيادة الألف بعد نون الجمع وقبل نون التأكيد، لئلا يجتمع ثلاث نونات متواليات.",
     "en": "So you say in the dual “iḍribānni”, keeping the alif, lest it be confused with the singular; and “iḍribnānni” in the feminine plural, adding an alif after the nūn of the plural and before the nūn of corroboration, lest three nūns come together in succession."},
    {"type": "matn",
     "ar": "(ولا تدخلهما) أي: التثنية والجمع المؤنث (النون الخفيفة) للزوم التقاء الساكنين على غير حده",
     "en": "(And the light nūn does not enter them), that is, the dual and the feminine plural, because a meeting of two quiescents not in its proper form would necessarily result,"},
    {"type": "matn",
     "ar": "(خلافا ليونس)، فإنه يجيز التقاء الساكنين على غير حده، ويجعله مغتفرا كما في الوقف، وليس بمرضي عند الأكثرين.",
     "en": "(in disagreement with Yūnus), for he permits the meeting of two quiescents not in its proper form and treats it as pardonable, as in pausal form (waqf); this is not accepted by most."},
    {"type": "matn",
     "ar": "(وهما) أي: النون الثقيلة والخفيفة (في غيرهما) أي: غير التثنية وجمع المؤنث (مع الضمير البارز) أي: واو جمع المذكر وياء المخاطبة (كالمنفصل) أي: كالكلمة المنفصلة،",
     "en": "(And the two), that is, the heavy and the light nūn, (in other than these two), that is, other than the dual and the feminine plural, (with the overt pronoun), that is, the wāw of the masculine plural and the yāʾ of the feminine addressee, (are like the separate), that is, like a separate word."},
    {"type": "matn",
     "ar": "يعني: يجب أن يعامل آخر الفعل مع النونين معاملته مع الكلمة المنفصلة من حذف الواو والياء أو تحريكهما ضما وكسرا،",
     "en": "He means: the end of the verb must be treated with the two nūns as it is treated with a separate word, by eliding the wāw and the yāʾ or by giving them a ḍamma and a kasra."},
    {"type": "matn",
     "ar": "وغرضه من هذا الكلام بيان أحوال الأفعال المعتلة الآخر عند إلحاق النون بها.",
     "en": "His purpose in this statement is to explain the states of verbs with a weak final letter when the nūn is attached to them."},
    {"type": "matn",
     "ar": "ومعنى كلامه: أن النونين حكمهما مع المثنى وجمع المؤنث ما ذكر، ومع غيرهما على ضربين:",
     "en": "The meaning of his statement is that the rule of the two nūns with the dual and the feminine plural is what was mentioned, and with others it is of two types:"},
]
