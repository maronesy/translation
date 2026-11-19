# -*- coding: utf-8 -*-
"""Mulla Jami — al-Fawāʾid al-Ḍiyāʾiyya. Source PDF page 273 (printed ٢٧٢)."""

PAGE_NUMBER = 273
PRINTED_PAGE = "٢٧٢"   # Arabic-Indic, as printed

BLOCKS = [
    # ---------------- The commentary text (matn) ----------------
    # Continues «(جاز» from the foot of PDF p. 272.
    {"type": "matn",
     "ar": "أن يكون ذلك) التمييز تارة (له) أي: للمنتصب عنه بأن يكون تمييزا يرفع الإبهام عنه[[١]]",
     "en": "…for that) specification sometimes (to belong to it), that is, to that from which it takes the accusative, by being a specification that removes the indefiniteness from it,"},
    {"type": "matn",
     "ar": "(و) تارة (لمتعلقه) بأن يكون تمييزا يرفع الإبهام[[٢]] عن متعلقه، وذلك بحسب القرائن والأحوال",
     "en": "(and) sometimes (to what is connected with it), by being a specification that removes the indefiniteness from what is connected with it; this depends on the contextual indications and circumstances,"},
    {"type": "matn",
     "ar": "مثل «أبا» في «طاب زيد أبا»، فإنه يصح أن يجعل عبارة عن «زيد»،",
     "en": "like “in respect of father” in “Zayd is good in respect of father,” for it can properly be taken as expressing “Zayd.”"},
    {"type": "matn",
     "ar": "فجاز أن يكون تارة تمييزا عن «زيد» إذا أريد إسناد الطيب إليه باعتبار أنه أبو عمرو، وجاز أن يكون تارة تمييزا عن متعلقه باعتبار أن الطيب مسند إلى متعلقه وهو أبوه.",
     "en": "So it may sometimes be a specification of “Zayd,” when attributing goodness to him is intended in respect of his being the father of ʿAmr; and it may sometimes be a specification of what is connected with him, in that goodness is attributed to what is connected with him, namely his father."},
    {"type": "matn",
     "ar": "(وإلا) أي: وإن لم يكن التمييز بعد ما لم يكن نصا في المنتصب عنه اسما يصح جعله لما انتصب عنه (فهو لمتعلقه) خاصة،",
     "en": "(Otherwise)—that is, if the specification, provided it is not explicitly [restricted] to that from which it takes the accusative, is not a noun that can properly be made to refer to that from which it takes the accusative—(it belongs to what is connected with it) exclusively,"},
    # REVIEW: print reads «في المنتصف عنه» (sense requires «المنتصب»); transcribed as printed.
    {"type": "matn",
     "ar": "نحو: «طاب زيد أبوة، ودارا، وعلما»، فإن هذه الأسماء ليست نصا في المنتصف عنه، ولا يصح جعلها له بالتعبير عنه بها،",
     "en": "as in “Zayd is good in fatherhood, in house and in knowledge”; for these nouns are not explicitly [restricted] to that from which it takes the accusative, nor can they properly be made to refer to it by expressing it by them."},
    {"type": "matn",
     "ar": "فهي لمتعلق «زيد»، وهو الذات المقدرة[[٣]]، أعني: الشيء المنسوب إلى «زيد»[[٤]].",
     "en": "So they belong to what is connected with “Zayd,” namely the implied entity—I mean, the thing attributed to “Zayd.”"},
    {"type": "matn",
     "ar": "(فيطابق) التمييز (فيهما) أي: فيما جاز[[٥]] أن يكون لما انتصب عنه سواء كان نصا فيه أو محتملا له ولمتعلقه، وفيما تعين لمتعلقه",
     "en": "(Then) the specification (agrees, in both)—that is, in what may belong to that from which it takes the accusative, whether explicitly restricted to it or admitting both it and what is connected with it, and in what is determined for what is connected with it—"},
    {"type": "matn",
     "ar": "(ما قصد) من وحدة التمييز وتثنيته وجمعيته سواء كان لموافقة ما انتصب عنه مثل: «طاب زيد أبا، والزيدان أبوين، والزيدون آباء»،",
     "en": "(with what is intended) of singularity, duality or plurality of the specification, whether this is to agree with that from which it takes the accusative, as in “Zayd is good as a father, the two Zayds as two fathers, and the Zayds as fathers,”"},
    {"type": "matn",
     "ar": "أو لمعنى في نفسه مثل قولك: «طاب زيد أبا» إذا أردت أبا له فقط، و«طاب زيد أبوين» إذا أردت أبا وجدا له، و«طاب زيد آباء» إذا أردت أبا وأجدادا له[[٦]]،",
     "en": "or for a meaning in itself, as when you say “Zayd is good in respect of father” when you mean only his father, “Zayd is good in respect of two fathers” when you mean his father and grandfather, and “Zayd is good in respect of fathers” when you mean his father and forefathers."},
    {"type": "matn",
     "ar": "فعلى كل من التقديرين إذا قصد وحدة التمييز أورد مفردا، وإذا قصد تثنيته، وإذا قصد جمعيته أورد جمعا، فإن صيغة المفرد لا يصلح أن يطلق على المثنى والمجموع",
     "en": "On each of the two interpretations, when singularity of the specification is intended, it is given in the singular; when its duality is intended, and when its plurality is intended, it is given in the plural; for the singular form is not fit to be applied to the dual and the plural,"},
    {"type": "matn",
     "ar": "(إلا إذا كان) التمييز (جنسا) يقع على القليل والكثير، فإنه إذا قصد تثنيته أو جمعيته لا",
     "en": "(except when) the specification (is a generic noun) applying to few and many; for when its duality or plurality is intended, it is not…"},

    {"type": "rule"},

    # ---------------- Footnote 1 ----------------
    {"type": "note", "num": "١"},
    {"type": "pair",
     "ar": "فيه مسامحة.",
     "en": "There is laxity of expression in this."},

    # ---------------- Footnote 2 ----------------
    {"type": "note", "num": "٢"},
    {"type": "pair",
     "ar": "فيه أنه لا إبهام فيما انتصب عنه، بل في الذات المقدرة.",
     "en": "Against this: there is no indefiniteness in that from which it takes the accusative, but rather in the implied entity."},
    {"type": "pair",
     "ar": "وكأنه أراد رفع الإبهام عن مبهم، هو نفس ما انتصب عنه.",
     "en": "It is as though he meant the removal of indefiniteness from an indefinite thing that is that very thing from which it takes the accusative."},

    # ---------------- Footnote 3 ----------------
    {"type": "note", "num": "٣"},
    {"type": "pair",
     "ar": "أي: المتعلق الذات المقدرة دون عين زيد.",
     "en": "That is, what is connected is the implied entity, not Zayd himself."},

    # ---------------- Footnote 4 ----------------
    {"type": "note", "num": "٤"},
    {"type": "pair",
     "ar": "تفسير للذات المقدرة التي حكم على المتعلق، فإنه هو حين كون التمييز لمتعلق ما انتصب عنه،",
     "en": "This explains the implied entity, which was predicated of what is connected, for it is that [connected thing] when the specification belongs to what is connected with that from which it takes the accusative;"},
    {"type": "pair",
     "ar": "فلا حاجة إلى تقييد الشيء المنسوب إلى زيد بكونه مغايرا له بناء على أن الشيء المنسوب إلى زيد، هو الذات المقدرة التي قد يكون عين زيد كما ظن.",
     "en": "so there is no need to restrict the thing attributed to Zayd to its being other than him, on the supposition that the thing attributed to Zayd is the implied entity, which may be Zayd himself, as has been thought."},

    # ---------------- Footnote 5 ----------------
    {"type": "note", "num": "٥"},
    {"type": "pair",
     "ar": "الظاهر أن ضمير «فيهما» راجع إلى القسمين المذكورين، فيبقى حكم ما كان نصا في المنتصب عنه،",
     "en": "It appears that the pronoun of “in both” refers back to the two divisions mentioned; so the ruling on what is explicitly [restricted] to that from which it takes the accusative is left [unstated];"},
    {"type": "pair",
     "ar": "فتكلف في مرجع الضمير بحيث يشتمل ما كان نصا. ولا يخفى أنه تعسف جدا.",
     "en": "so he strained the referent of the pronoun so that it includes what is explicit. It is not hidden that this is highly forced."},

    # ---------------- Footnote 6 ----------------
    {"type": "note", "num": "٦"},
    {"type": "pair",
     "ar": "المراد بالأجداد: ما فوق الواحد.",
     "en": "What is meant by “forefathers” is more than one."},
]
