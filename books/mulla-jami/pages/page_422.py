# -*- coding: utf-8 -*-
"""Mulla Jami — al-Fawāʾid al-Ḍiyāʾiyya. Source PDF page 422 (printed ٤٢١)."""

PAGE_NUMBER = 422
PRINTED_PAGE = "٤٢١"   # Arabic-Indic, as printed

BLOCKS = [
    # ---------------- The commentary text (matn) ----------------
    # Continues «ولم يذكره المتقدمون؛ لرجوعه إلى ذي اللام؛ إذ» at the foot of PDF p. 421.
    {"type": "matn",
     "ar": "أصل «يا رجل»[[١]]: يا أيها الرجل.",
     "en": "…the origin of “yā rajulu” is “yā ayyuhā l-rajulu” (O you man!)."},
    {"type": "matn",
     "ar": "(و) السادس: (المضاف إلى أحدها) أي: إلى أحد الأمور الخمسة المذكورة،",
     "en": "(And) the sixth: (what is annexed to one of them), that is, to one of the five things mentioned."},
    {"type": "matn",
     "ar": "ولا يستلزم صحة الإضافة إلى أحدها صحتها بالنسبة إلى كل واحد، فلا يرد أنها لا تصح إلا بالنسبة إلى الأربع الأول، فإن المنادى لا يضاف إليه.",
     "en": "The validity of annexation to one of them does not entail its validity with respect to each one; so the objection does not arise that it is valid only with respect to the first four, since nothing is annexed to the vocative noun (munādā)."},
    {"type": "matn",
     "ar": "قيل: كان عليه أن يقول: «والمضاف إلى المعرفة» ليدخل فيه المضاف إلى المضاف إلى المعرفة أيضا مثل: «غلام أبيك»؟",
     "en": "It has been said: should he not have said “and what is annexed to a definite noun”, so that what is annexed to a noun annexed to a definite noun would also be included, as in “ghulāmu abīka” (your father’s servant)?"},
    {"type": "matn",
     "ar": "والجواب: أن المراد بالمضاف إلى أحدها أعم من أن يكون بالذات أو بالواسطة،",
     "en": "The answer: what is meant by “what is annexed to one of them” is more general than its being so directly or through an intermediary."},
    {"type": "matn",
     "ar": "ولا يخفى عليك نظرا إلى ما سبق أن المضاف إذا كان لفظ الغير أو المثل أو الشبه؛ فهو مستثنى من هذا الحكم[[٢]]",
     "en": "In view of what has preceded, it will not be hidden from you that if the annexed noun is the word ghayr (other), mithl (like) or shibh (similar), it is excepted from this ruling."},
    {"type": "matn",
     "ar": "(معنى) أي: إضافة معنى، يعني: إضافة معنوية.",
     "en": "(In meaning), that is, an annexation of meaning, namely a semantic annexation (iḍāfa maʿnawiyya)."},
    {"type": "matn",
     "ar": "فقوله: «معنى» مفعول مطلق بحذف مضاف. واحترز به عن المضاف إلى أحد هذه الأمور إضافة لفظية، فإنها لا تفيد تعريفا.",
     "en": "So his word “maʿnan” is an absolute object (mafʿūl muṭlaq) with an annexed noun elided. By it he excludes what is annexed to one of these things by a formal annexation (iḍāfa lafẓiyya), for that does not convey definiteness."},
    {"type": "matn",
     "ar": "ولما سبق تعريف المضمرات، والمهبمات، ومعنى المضاف إلى أحدها معنى ظاهر، والمعرف باللام والنداء مستغن عن التعريف، خص العلم بالتعريف",
     "en": "Since the definition of the pronouns and of the vague nouns has preceded, the meaning of “what is annexed to one of them in meaning” is evident, and what is made definite by the lām and by the vocative needs no definition, he singled out the proper name for definition."},
    # REVIEW: «والمهبمات» is printed with the bāʾ and hāʾ transposed (for «والمبهمات»); transcribed as printed.
    {"type": "matn",
     "ar": "(و) قال (العلم) اسما كان[[٣]] أو لقبا أو كنية؛",
     "en": "(And) he said: (the proper name (ʿalam)), whether it is a name (ism), an epithet (laqab) or a patronymic (kunya);"},
    {"type": "matn",
     "ar": "لأنه إن صدر بالأب أو الأم[[٤]] أو الابن أو البنت فهو كنية، وإلا فإن قصد به[[٥]] مدح أو ذم فهو اللقب، وإلا فهو الاسم",
     "en": "for if it begins with “father”, “mother”, “son” or “daughter”, it is a kunya; otherwise, if praise or blame is intended by it, it is the laqab; otherwise it is the ism:"},
    {"type": "matn",
     "ar": "(ما وضع لشيء بعينه) شخصا أو جنسا.",
     "en": "(what is imposed for a thing in its very identity), whether an individual or a genus."},
    {"type": "matn",
     "ar": "واحترز به عن النكرات، والأعلام الغالبة التي تعينت لفرد معين بغلبة",
     "en": "By this he excludes indefinite nouns, and the predominant proper names (al-aʿlām al-ghāliba) that have become fixed for a specific individual through predominance…"},

    {"type": "rule"},

    # ---------------- Footnote 1 ----------------
    {"type": "note", "num": "١"},
    {"type": "pair",
     "ar": "يعني: أنه كان في الأصل معرفا باللام، ثم توسل لندائه بأي، ثم حذف اللام، وأي لكثرة الاستعمال فصار: «يا رجل».",
     "en": "That is: it was originally made definite by the lām; then ayy was used as a means to call it in the vocative; then the lām and ayy were elided because of frequent use, and it became “yā rajulu”."},

    # ---------------- Footnote 2 ----------------
    {"type": "note", "num": "٢"},
    {"type": "pair",
     "ar": "جزاء «إذا» والشرطية خبر «أن».",
     "en": "[It is] the apodosis of “idhā”, and the conditional sentence is the predicate of “anna”."},
    {"type": "pair",
     "ar": "ولو قال المصنف: وما عرف باللام والنداء والإضافة لكان أخصر وأتم،",
     "en": "Had the author said “and what is made definite by the lām, the vocative and annexation”, it would have been more concise and more complete."},
    {"type": "pair",
     "ar": "ولا يبعد أن يجعل المضاف مصدرا ميميا في معنى الإضافة معطوفا على اللام، فيكون في معنى، وما عرف بالإضافة معنى.",
     "en": "It is not far-fetched to take al-muḍāf as a mīm-initial verbal noun (maṣdar mīmī) in the sense of “annexation”, coordinated with “the lām”; it would then mean: “and what is made definite by annexation in meaning”."},

    # ---------------- Footnote 3 ----------------
    {"type": "note", "num": "٣"},
    {"type": "pair",
     "ar": "هذا معنى ثالث للاسم أخص من العلم، فله معان ثلاثة مترتبة في العموم، وقد عرفتها فاحفظها.",
     "en": "This is a third meaning of ism, more specific than “proper name”; so it has three meanings ranked in generality. You have come to know them, so retain them."},

    # ---------------- Footnote 4 ----------------
    {"type": "note", "num": "٤"},
    {"type": "pair",
     "ar": "هكذا في كتب النحو، لكن قال صاحب القاموس: أبو العتابية ككراهية لقب أبي إسحاق إسماعيل بن سويد لا كنيته، ووهم الجوهري هذا، فاحفظه، فإنه بديع.",
     "en": "So it is in the books of grammar; but the author of al-Qāmūs said: “Abū l-ʿAtāhiya”—on the pattern of karāhiya—is the laqab of Abū Isḥāq Ismāʿīl ibn Suwayd, not his kunya, and al-Jawharī erred in this. Retain this, for it is remarkable."},
    # REVIEW: printed «أبو العتابية» (with tāʾ and bāʾ); the poet's name is normally Abū l-ʿAtāhiya, and «ككراهية» fits that form. Also «بن سويد»: the poet is usually Ismāʿīl ibn al-Qāsim ibn Suwayd. Transcribed as printed.

    # ---------------- Footnote 5 ----------------
    {"type": "note", "num": "٥"},
    {"type": "pair",
     "ar": "أي: حين الوضع لا حين الاستعمال؛ لأنه قد يطلق اللقب على المسمى من غير قصد المدح والذم،",
     "en": "That is, at the time of imposition, not at the time of use; for the laqab is sometimes applied to the one named without intending praise or blame,"},
    {"type": "pair",
     "ar": "ولأنه قد يقصد بالاسم في الاستعمال المدح والذم إذا اشتهر المسمى في ضمنه بصفة مدح أو ذم نحو: حاتم،",
     "en": "and because praise or blame is sometimes intended by the ism in use, when the one named has become famous under it for a praiseworthy or blameworthy quality, as with Ḥātim."},
    {"type": "pair",
     "ar": "وقصد الواضع يفهم من كونه منقولا من معناه الأصلي إلى المعنى العلمي، فإن المنقولات يلاحظ فيها المعاني الأصلية.",
     "en": "The imposer’s intention is understood from its having been transferred from its original meaning to the meaning of a proper name, for in transferred words (manqūlāt) the original meanings are taken into consideration."},
]
