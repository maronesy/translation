# -*- coding: utf-8 -*-
"""Mulla Jami — al-Fawāʾid al-Ḍiyāʾiyya. Source PDF page 254 (printed ٢٥٣)."""

PAGE_NUMBER = 254
PRINTED_PAGE = "٢٥٣"   # Arabic-Indic, as printed

BLOCKS = [
    # ---------------- The commentary text (matn) ----------------
    # Continues «نحو قوله تعالى: ﴿فيها يفرق كل» from the foot of PDF p. 253.
    {"type": "matn",
     "ar": "أمر حكيم، أمرا من عندنا﴾[[١]] إن جعلت «أمرا» حالا[[٢]] من «كل أمر»",
     "en": "…wise matter, as a command from Us,” if you make “amran” a ḥāl of “every matter”;"},
    {"type": "matn",
     "ar": "أو واقعة في حيز الاستفهام[[٣]] نحو: «هل أتاك رجل راكبا»،",
     "en": "or [an indefinite] falling within the scope of an interrogative, as in “Did a man come to you, riding?”;"},
    {"type": "matn",
     "ar": "أو بعد «إلا» نقضا للنفي[[٤]]، نحو: «ما جاءني رجل إلا راكبا»،",
     "en": "or after “illā” breaking a negation, as in “No man came to me except riding”;"},
    {"type": "matn",
     "ar": "أو مقدما عليه الحال[[٥]] نحو: «جاءني راكبا رجل».",
     "en": "or with the ḥāl placed before it, as in “There came to me, riding, a man.”"},
    {"type": "matn",
     "ar": "وثانيهما: ما يكون ذو الحال فيه غير هذه الأمور، وغالب مواد وقوع الحال وأكثرها هو هذا القسم،",
     "en": "The second: that in which the owner of the ḥāl is other than these; and the majority and most of the instances in which a ḥāl occurs belong to this kind,"},
    {"type": "matn",
     "ar": "ووقوع الحال في هذا القسم مشروط بكون صاحبها معرفة،",
     "en": "and the occurrence of the ḥāl in this kind is conditional on its owner being definite."},
    {"type": "matn",
     "ar": "فقوله: «غالبا» قيد لاشتراط كون صاحبها معرفة، لا لكون صاحبها معرفة",
     "en": "So his word “for the most part” qualifies the stipulation that its owner be definite, not the owner’s being definite [itself],"},
    {"type": "matn",
     "ar": "حتى يقال: إن غالبية كون صاحبها معرفة المنبئة عن تخلفه في بعض المواد تنافي الشرطية،",
     "en": "such that it might be said: the owner’s being definite “for the most part,” which indicates its failing in some instances, is incompatible with its being a condition,"},
    {"type": "matn",
     "ar": "ويحتاج إلى أن يصرف الكلام عن ظاهره، ويجعل قوله: «وصاحبها[[٦]] معرفة» مبتدأ وخبرا معطوفا على قوله: «وشرطها: أن تكون نكرة».",
     "en": "and that the speech would need to be turned from its apparent sense, with his words “and its owner is definite” taken as a mubtadaʾ and khabar conjoined to his words “and its condition is that it be indefinite.”"},
    {"type": "verse",
     "ar": "(وأرسلها العراك[[٧]]) ولم يذدها[[٨]]          ولم يشفق على نغص الدخال[[٩]]",
     "en": "(And he sent them in a crowd, al-ʿirāk) and did not drive them back, / nor feared the spoiling of the crowding at the water (al-dikhāl)."},

    {"type": "rule"},

    # ---------------- Footnote 1 ----------------
    {"type": "note", "num": "١"},
    {"type": "pair",
     "ar": "سورة الدخان: ٤-٥.",
     "en": "Qurʾān, Sūrat al-Dukhān 44:4–5."},

    # ---------------- Footnote 2 ----------------
    {"type": "note", "num": "٢"},
    {"type": "pair",
     "ar": "أشار به إلى أنه ليس نصا في الاستشهاد لجواز أن يكون منصوبا على الاختصاص،",
     "en": "By this he indicated that it is not explicit proof for the point, since it may be in the accusative by way of specification (ikhtiṣāṣ),"},
    {"type": "pair",
     "ar": "أو على الحال عن ضمير الفاعل في «أنزلناه» أي: آمرين أمرا، أو عن ضمير مفعوله.",
     "en": "or as a ḥāl of the agent pronoun in “anzalnāhu” (We sent it down), that is, “commanding a command,” or of its object pronoun."},
    {"type": "pair",
     "ar": "لا يخفى أنك لو جعلت حالا من كل أمر ليس أيضا نصا في المقصود لجواز أن يكون حالا عنه من حيث إنه مخصوص بالإضافة أو بالوصف.",
     "en": "It is not hidden that even if you make it a ḥāl of “every matter,” it is again not explicit for the intended point, since it may be a ḥāl of it inasmuch as it is specified by annexation or by qualification."},

    # ---------------- Footnote 3 ----------------
    {"type": "note", "num": "٣"},
    {"type": "pair",
     "ar": "لأنها تشبه النكرة الواقعة في حيز النفي في كونها غير موجبة.",
     "en": "Because it resembles the indefinite falling within the scope of a negation in being non-affirmative."},

    # ---------------- Footnote 4 ----------------
    {"type": "note", "num": "٤"},
    {"type": "pair",
     "ar": "لم يغير قدس سره في تعيين صورة النكرة عبارة اللباب حيث قال:",
     "en": "He—may his secret be sanctified—did not alter the wording of al-Lubāb in specifying the forms of the indefinite, where it says:"},
    {"type": "pair",
     "ar": "لا يكون أي: صاحب الحال إلا نكرة موصوفة، أو مغنية غناء المعرفة لاستغراقها، أو في حيز الاستفهام، أو بعد إلا نقضا للنفي، أو مقدما عليه الحال، انتهى.",
     "en": "“It”—that is, the owner of the ḥāl—“is not [indefinite] except as a qualified indefinite, or one that suffices as a definite because of its all-inclusiveness, or within the scope of an interrogative, or after illā breaking a negation, or with the ḥāl placed before it.” End of quotation."},

    # ---------------- Footnote 5 ----------------
    {"type": "note", "num": "٥"},
    {"type": "pair",
     "ar": "إنما حسن التنكير حينئذ؛ لأن التقديم يؤمن الالتباس بالصفة.",
     "en": "Indefiniteness is acceptable in that case only because preposing guards against confusion with an adjective."},

    # ---------------- Footnote 6 ----------------
    {"type": "note", "num": "٦"},
    # REVIEW: print reads «أو معنى فعلى» (perhaps for «فعلي»); transcribed as printed.
    {"type": "pair",
     "ar": "وحينئذ يكون غالبا ظرفا للنسبة بين المبتدأ والخبر، أو معنى فعلى مستفاد من قوله: معرفة أي: يتعرف غالبا.",
     "en": "In that case “for the most part” would be an adverbial qualifying the predication between the mubtadaʾ and the khabar, or a verbal meaning derived from his word “definite,” that is, “it is made definite for the most part.”"},

    # ---------------- Footnote 7 ----------------
    {"type": "note", "num": "٧"},
    {"type": "pair",
     "ar": "أورد أمثلة موثوقا بها للنقض الأول من شعر لبيد، والثاني مما شاع في المحاورات والمخاطبات.",
     "en": "He adduced reliable examples for the objection: the first from the poetry of Labīd, and the second from what is current in conversation and address."},
    # REVIEW: print reads «إما الاشتهار البيت» (sense suggests «لاشتهار»); transcribed as printed.
    {"type": "pair",
     "ar": "ولم يورد الأول على وجه يشعر بشعريته إما الاشتهار البيت فيما بينهم بحيث يكفي الإشارة إليه، وإما لأنها أيضا شائع في المحاورات بحيث لا يحتاج إلى التمسك بوقوعه في شعر البليغ.",
     "en": "He did not cite the first in a way that signals its being poetry, either because the verse is so well known among them that alluding to it suffices, or because it too is current in conversation, so that there is no need to rely on its occurring in the poetry of an eloquent poet."},
    # REVIEW: print reads «أورد أبله» (sense «إبله»); transcribed as printed.
    {"type": "pair",
     "ar": "قال صاحب القاموس: يقال: أورد أبله العراك أي: أوردها للماء جميعا.",
     "en": "The author of al-Qāmūs said: one says “he brought his camels to water al-ʿirāk,” that is, he brought them to the water all together."},
    {"type": "pair",
     "ar": "والأصل عراكا، فأدخل «ال»، ولم يتغير معنى المصدر، هذا كلامه.",
     "en": "The base form is “ʿirākan”; “al” was added and the meaning of the verbal noun did not change. These are his words."},

    # ---------------- Footnote 8 ----------------
    {"type": "note", "num": "٨"},
    # REVIEW: print reads «الزوج المنع» (the gloss of «يذدها» would be «الذود»); transcribed as printed.
    {"type": "pair",
     "ar": "قال قدس سره في الحاشية: الزوج المنع.",
     "en": "He—may his secret be sanctified—said in the gloss: “al-zawj” [sic; i.e. al-dhawd] is preventing."},

    # ---------------- Footnote 9 ----------------
    {"type": "note", "num": "٩"},
    {"type": "pair",
     "ar": "قال قدس سره في الحاشية: الإشفاق: الخوف.",
     "en": "He—may his secret be sanctified—said in the gloss: ishfāq is fear."},
    {"type": "pair",
     "ar": "والنغص بالصاد المهملة والغين المعجمة المفتوحة من نغص الرجل نغصا أي: لم يتم مراده، انتهى.",
     "en": "Al-naghaṣ, with the undotted ṣād and the dotted ghayn bearing fatḥa, is from “naghiṣa al-rajul naghaṣan,” that is, his aim was not fulfilled. End of quotation."},
]
