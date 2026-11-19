# -*- coding: utf-8 -*-
"""Mulla Jami — al-Fawāʾid al-Ḍiyāʾiyya. Source PDF page 480 (printed ٤٧٩)."""

PAGE_NUMBER = 480
PRINTED_PAGE = "٤٧٩"   # Arabic-Indic, as printed

BLOCKS = [
    {"type": "section", "ar": "[الفعل]",
     "en": "The Verb (al-Fiʿl)"},

    # ---------------- The commentary text (matn) ----------------
    {"type": "matn",
     "ar": "ولما قسم المصنف الكلمة[[١]] إلى أقسامها الثلاثة[[٢]] على وجه[[٣]] علم من دليل الانحصار حد كل واحد[[٤]] منها[[٥]]،",
     "en": "Since the author divided the word (kalima) into its three divisions in such a way that the definition of each one of them was known from the proof of the restriction [to three],"},
    {"type": "matn",
     "ar": "ولم يكتف[[٦]] بذلك القدر، بل صدر مباحث الاسم بتعريفه.",
     "en": "and did not content himself with that much, but opened the discussions of the noun with its definition,"},
    {"type": "matn",
     "ar": "فلما وصلت النوبة إلى مباحث الفعل، سلك تلك الطريقة[[٧]]، وصدرها بتعريفه،",
     "en": "so when the turn came to the discussions of the verb, he followed that same method and opened them with its definition,"},
    {"type": "matn",
     "ar": "فقال: (الفعل: ما دل) أي: كلمة[[٨]] دلت (على معنى) كائن[[٩]] (في نفسه) أي: في نفس ما دل، يعني: الكلمة.",
     "en": "saying: (The verb is what indicates), that is, a word that indicates, (a meaning) that is (in itself), that is, in the very thing that indicates, namely the word."},
    {"type": "matn",
     "ar": "والمراد بكون المعنى[[١٠]] في نفس الكلمة: دلالتها عليه[[١١]] من غير حاجة إلى",
     "en": "What is meant by the meaning’s being in the word itself is the word’s indicating it without need of…"},

    {"type": "rule"},

    # ---------------- Footnote 1 ----------------
    {"type": "note", "num": "١"},
    {"type": "pair",
     "ar": "في صدر الكتاب.",
     "en": "At the opening of the book."},

    # ---------------- Footnote 2 ----------------
    {"type": "note", "num": "٢"},
    {"type": "pair",
     "ar": "أي: الاسم والفعل والحرف.",
     "en": "That is, the noun, the verb and the particle."},

    # ---------------- Footnote 3 ----------------
    {"type": "note", "num": "٣"},
    {"type": "pair",
     "ar": "«على» بمعنى «في» كما في قوله تعالى: ﴿حقيق على أن لا أقول﴾ (الأعراف: ١٠٥) أي: في تقسيم علم من دليل انحصاره.",
     "en": "“ʿAlā” has the sense of “fī”, as in His words, the Exalted: “It is right that I say not [about Allah except the truth]” (Qurʾān, Sūrat al-Aʿrāf 7:105); that is, in a division [such that the definitions] were known from the proof of its restriction."},
    {"type": "pair",
     "ar": "فاللام عوض عن الضمير، فلا يلزم خلو الجملة الصفتية عن الضمير،",
     "en": "So the definite article [in «الانحصار»] stands in place of the pronoun, and it does not follow that the adjectival clause lacks a pronoun."},
    {"type": "pair",
     "ar": "والصفة وإن كانت كافية في معلومية حدود ذات تلك الأقسام، لكن معلوميتها من حيث إنها حدود لأقسام الكلمة موقوفة على التقسيم،",
     "en": "Although the adjectival clause suffices for knowing the definitions of the essence of those divisions, knowing them insofar as they are definitions of the divisions of the word depends on the division;"},
    {"type": "pair",
     "ar": "فلا يرد ألا مدخل للتقسيم في معلومية الحدود.",
     "en": "so the objection that the division has no part in knowing the definitions does not arise."},

    # ---------------- Footnote 4 ----------------
    {"type": "note", "num": "٤"},
    {"type": "pair",
     "ar": "أي: من الأقسام الثلاثة.",
     "en": "That is, of the three divisions."},

    # ---------------- Footnote 5 ----------------
    {"type": "note", "num": "٥"},
    {"type": "pair",
     "ar": "بعد تكميل مباحث الاسم.",
     "en": "After completing the discussions of the noun."},

    # ---------------- Footnote 6 ----------------
    {"type": "note", "num": "٦"},
    {"type": "pair",
     "ar": "المصنف.",
     "en": "[That is,] the author."},

    # ---------------- Footnote 7 ----------------
    {"type": "note", "num": "٧"},
    {"type": "pair",
     "ar": "أي: هو بصدد بيان الأقسام على طريقة واحدة،",
     "en": "That is, he is concerned with setting out the divisions according to a single method;"},
    {"type": "pair",
     "ar": "مما يدل على أنه بصدد ذلك أنه ذكر بعد تعريف الفعل بعض خواصه، كما فعل ذلك في قسم الاسم، والله أعلم.",
     "en": "what shows that he is concerned with this is that after the definition of the verb he mentioned some of its properties, as he did in the section on the noun. And Allah knows best."},
    {"type": "pair",
     "ar": "قال عبد الحكيم: أي: عدم الاكتفاء بمعلومية تعريفه عن الدليل،",
     "en": "ʿAbd al-Ḥakīm said: that is, not being content with its definition’s being known from the proof;"},
    {"type": "pair",
     "ar": "فلا يلزم التخصيص بلا مخصص لاستواء الكل في كونها أقساما للكلمة معلومة تعريفاتها من الدليل.",
     "en": "so there is no specification without a specifier, since all are equal in being divisions of the word whose definitions are known from the proof."},

    # ---------------- Footnote 8 ----------------
    {"type": "note", "num": "٨"},
    {"type": "pair",
     "ar": "جمع ما بين «ما دل» و«الكلمة» في التفسير إشارة معرفة وجه تذكير الضمير، وهو أنه باعتبار لفظ «ما دل» دون معناه.",
     "en": "He combined “mā dalla” and “the word” in the explanation to indicate the reason for the masculine pronoun, namely that it is with regard to the wording of “mā dalla”, not its meaning."},

    # ---------------- Footnote 9 ----------------
    {"type": "note", "num": "٩"},
    {"type": "pair",
     "ar": "إشارة إلى أن قوله: «في نفسه» ظرف مستقر صفة لـ«معنى»، ولم يجعله حالا؛ إذ ليس المعنى على التقييد",
     "en": "An indication that his words “fī nafsihi” are a fixed adverbial (ẓarf mustaqarr) serving as an adjective of “maʿnā”; he did not make it a circumstantial qualifier, since the meaning is not one of restriction,"},
    {"type": "pair",
     "ar": "ولا متعلقا بـ«دل» لاحتياجه إلى جعل «في» بمعنى الباء.",
     "en": "nor attached to “dalla”, because that would require taking “fī” in the sense of the bāʾ."},

    # ---------------- Footnote 10 ----------------
    {"type": "note", "num": "١٠"},
    # REVIEW: printed «حتى يراد» (and «صيغة المعنى»); the sense seems to call for «حتى يرد» (“so that the objection arises”). Transcribed as printed; translated by the apparent sense.
    {"type": "pair",
     "ar": "أي: المقصود به. والحاصل منه ذلك لأنه مفسر به حتى يراد أن صيغة المعنى كيف تفسر بصفة اللفظ،",
     "en": "That is, what is intended by it. The upshot of it is that, because [the meaning] is explained by it, it would be objected: how can the form of the meaning be explained by an attribute of the expression,"},
    {"type": "pair",
     "ar": "وأنه يصير المعنى ما دل على معنى دلت عليه الكلمة بالاستقلال، ويحتاج إلى تكلفات باردة تمجها الأسماع.",
     "en": "and that the meaning would become “what indicates a meaning that the word indicates independently”, requiring cold contrivances that the ears reject."},

    # ---------------- Footnote 11 ----------------
    {"type": "note", "num": "١١"},
    {"type": "pair",
     "ar": "فالكلمة محيطة بالمعنى إحاطة الظرف بالمظروف من حيث إنه لا يخرج فهم المعنى عنها.",
     "en": "So the word encompasses the meaning as a container encompasses what it contains, in that the understanding of the meaning does not go outside it."},
]
